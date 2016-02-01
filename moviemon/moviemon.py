
"""moviemon.

Usage:
  moviemon PATH
  moviemon [-i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
  moviemon -h | --help
  moviemon --version

Options:
  -h, --help            Show this screen.
  --version             Show version.
  PATH                  Path to movies dir. to index/reindex all movies.
  -i, --imdb            Sort acc. to IMDB rating.(dec)
  -t, --tomato          Sort acc. to Tomato Rotten rating.(dec)
  -g, --genre           Show movie name with its genre.
  -a, --awards          Show movie name with awards recieved.
  -c, --cast            Show movie name with its cast.
  -d, --director        Show movie name with its director(s).
  -y, --year            Show movie name with its release date.
  -r, --runtime         Show movie name with its runtime.
  -I, --imdb-rev        Sort acc. to IMDB rating.(inc)
  -T, --tomato-rev      Sort acc. to Tomato Rotten rating.(inc)

"""

from __future__ import print_function
import os
import textwrap
import requests
import json
from guessit import guess_file_info
from terminaltables import AsciiTable
try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode
from docopt import docopt
from tqdm import tqdm
from colorama import init, Fore

init()

OMDB_URL = 'http://www.omdbapi.com/?'

EXT = (".3g2 .3gp .3gp2 .3gpp .60d .ajp .asf .asx .avchd .avi .bik .bix"
       ".box .cam .dat .divx .dmf .dv .dvr-ms .evo .flc .fli .flic .flv"
       ".flx .gvi .gvp .h264 .m1v .m2p .m2ts .m2v .m4e .m4v .mjp .mjpeg"
       ".mjpg .mkv .moov .mov .movhd .movie .movx .mp4 .mpe .mpeg .mpg"
       ".mpv .mpv2 .mxf .nsv .nut .ogg .ogm .omf .ps .qt .ram .rm .rmvb"
       ".swf .ts .vfw .vid .video .viv .vivo .vob .vro .wm .wmv .wmx"
       ".wrap .wvx .wx .x264 .xvid")

EXT = tuple(EXT.split())

CONFIG_PATH = os.path.expanduser("~/.moviemon")


def main():
    args = docopt(__doc__, version='moviemon 1.0.10')
    util(args)


def util(docopt_args):
    if docopt_args["PATH"]:
        if os.path.isdir(docopt_args["PATH"]):

            print("\n\nIndexing all movies inside ",
                  docopt_args["PATH"] + "\n\n")

            dir_json = docopt_args["PATH"] + ".json"

            # Save path to config file so we can read it later
            with open(CONFIG_PATH, "w") as inpath:
                inpath.write(docopt_args["PATH"])

            scan_dir(docopt_args["PATH"], dir_json)

            if movie_name:
                if movie_not_found:
                    print(Fore.RED + "\n\nData for the following movie(s)"
                          " could not be fetched -\n")
                    for val in movie_not_found:
                        print(Fore.RED + val)
                if not_a_movie:
                    print(Fore.RED + "\n\nThe following media in the"
                          " folder is not movie type -\n")
                    for val in not_a_movie:
                        print(Fore.RED + val)
                print(Fore.GREEN + "\n\nRun $moviemon\n\n")
            else:
                print(Fore.RED + "\n\nGiven directory does not contain movies."
                      " Pass a directory containing movies\n\n")
        else:
            print(Fore.RED + "\n\nDirectory does not exists."
                  " Please pass a valid directory containing movies.\n\n")

    elif docopt_args["--imdb"]:
        table_data = [["TITLE", "IMDB RATING"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"] = clean_table(item["Title"], None, item,
                                        table)
            table_data.append([item["Title"], item["imdbRating"]])
        sort_table(table_data, 1, True)

    elif docopt_args["--tomato"]:
        table_data = [["TITLE", "TOMATO RATING"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"] = clean_table(item["Title"], None, item,
                                        table)
            table_data.append([item["Title"], item["tomatoRating"]])
        sort_table(table_data, 1, True)

    elif docopt_args["--genre"]:
        table_data = [["TITLE", "GENRE"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"] = clean_table(item["Title"], None,
                                        item, table)
            table_data.append([item["Title"], item["Genre"]])
        sort_table(table_data, 0, False)

    elif docopt_args["--awards"]:
        table_data = [["TITLE", "AWARDS"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"], item["Awards"] = clean_table(item["Title"],
                                                        item["Awards"], item,
                                                        table)
            table_data.append([item["Title"], item["Awards"]])
        sort_table(table_data, 0, False)

    elif docopt_args["--cast"]:
        table_data = [["TITLE", "CAST"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"], item["Actors"] = clean_table(item["Title"],
                                                        item["Actors"], item,
                                                        table)
            table_data.append([item["Title"], item["Actors"]])
        sort_table(table_data, 0, False)

    elif docopt_args["--director"]:
        table_data = [["TITLE", "DIRECTOR(S)"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"], item["Director"] = clean_table(item["Title"],
                                                          item["Director"],
                                                          item, table)
            table_data.append([item["Title"], item["Director"]])
        sort_table(table_data, 0, False)

    elif docopt_args["--year"]:
        table_data = [["TITLE", "RELEASED"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"] = clean_table(item["Title"], None, item,
                                        table)
            table_data.append([item["Title"], item["Released"]])
        sort_table(table_data, 0, False)

    elif docopt_args["--runtime"]:  # Sort result by handling numeric sort
        table_data = [["TITLE", "RUNTIME"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"] = clean_table(item["Title"], None, item,
                                        table)
            table_data.append([item["Title"], item["Runtime"]])
        print_table(table_data)

    elif docopt_args["--imdb-rev"]:
        table_data = [["TITLE", "IMDB RATING"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"] = clean_table(item["Title"], None, item,
                                        table)
            table_data.append([item["Title"], item["imdbRating"]])
        sort_table(table_data, 1, False)

    elif docopt_args["--tomato-rev"]:
        table_data = [["TITLE", "TOMATO RATING"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"] = clean_table(item["Title"], None, item,
                                        table)
            table_data.append([item["Title"], item["tomatoRating"]])
        sort_table(table_data, 1, False)

    else:
        table_data = [
            ["TITLE", "GENRE", "IMDB", "RUNTIME", "TOMATO",
             "YEAR"]]
        data, table = butler(table_data)
        for item in data:
            item["Title"], item["Genre"] = clean_table(item["Title"],
                                                       item["Genre"], item,
                                                       table)
            table_data.append([item["Title"], item["Genre"],
                               item["imdbRating"], item["Runtime"],
                               item["tomatoRating"], item["Year"]])
        sort_table(table_data, 0, False)


def sort_table(table_data, index, reverse):
    table_data = (table_data[:1] + sorted(table_data[1:],
                                          key=lambda i: i[index],
                                          reverse=reverse))
    print_table(table_data)


def clean_table(tag1, tag2, item, table):
    if tag1 and tag2:
        if len(tag1) > table.column_max_width(0):
            tag1 = textwrap.fill(
                tag1, table.column_max_width(0))
            if len(tag2) > table.column_max_width(1):
                tag2 = textwrap.fill(
                    tag2, table.column_max_width(1))
        elif len(tag2) > table.column_max_width(1):
            tag2 = textwrap.fill(
                tag2, table.column_max_width(1))
        return tag1, tag2
    elif tag1:
        if len(tag1) > table.column_max_width(0):
            tag1 = textwrap.fill(
                tag1, table.column_max_width(0))
        return tag1


def butler(table_data):
    try:
        with open(CONFIG_PATH) as config:
            movie_path = config.read()
    except IOError:
        print(Fore.RED, "\n\nRun `$moviemon PATH` to "
              "index your movies directory.\n\n")
        quit()
    else:
        table = AsciiTable(table_data)
        try:
            with open(movie_path + ".json") as inp:
                data = json.load(inp)
            return data, table
        except IOError:
            print(Fore.YELLOW, "\n\nRun `$moviemon PATH` to "
                  "index your movies directory.\n\n")
            quit()


def print_table(table_data):
    table = AsciiTable(table_data)
    table.inner_row_border = True
    if table_data[:1] in ([['TITLE', 'IMDB RATING']],
                          [['TITLE', 'TOMATO RATING']]):
        table.justify_columns[1] = 'center'
    print("\n")
    print(table.table)


movies = []
movie_name = []
not_a_movie = []
movie_not_found = []


def scan_dir(path, dir_json):
    # Preprocess the total files count
    for root, dirs, files in tqdm(os.walk(path)):
        for name in files:
            path = os.path.join(root, name)
            if os.path.getsize(path) > (25*1024*1024):
                ext = os.path.splitext(name)[1]
                if ext in EXT:
                    movie_name.append(name)

    with tqdm(total=len(movie_name), leave=True, unit='B',
              unit_scale=True) as pbar:
        for name in movie_name:
            data = get_movie_info(name)
            pbar.update()
            if data is not None and data['Response'] == 'True':
                for key, val in data.items():
                    if val == "N/A":
                        data[key] = "-"  # Should N/A be replaced with `-`?
                movies.append(data)
            else:
                if data is not None:
                    movie_not_found.append(name)
        with open(dir_json, "w") as out:
            json.dump(movies, out, indent=2)


def get_movie_info(name):
    """Find movie information"""
    movie_info = guess_file_info(name)
    if movie_info['type'] == "movie":
        if 'year' in movie_info:
            return omdb(movie_info['title'], movie_info['year'])
        else:
            return omdb(movie_info['title'], None)
    else:
        not_a_movie.append(name)


def omdb(title, year):
    """ Fetch data from OMDB API. """
    params = {'t': title.encode('ascii', 'ignore'),
              'plot': 'full',
              'type': 'movie',
              'tomatoes': 'true'}

    if year:
        params['y'] = year

    url = OMDB_URL + urlencode(params)
    return json.loads(requests.get(url).text)

if __name__ == '__main__':
    main()