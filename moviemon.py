"""moviemon.

Usage:
  moviemon.py PATH
  moviemon.py --index
  moviemon.py [-i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
  moviemon.py -h
  moviemon.py --version

Options:
  -h, --help            Show this screen.
  -v, --version         Show version.
  PATH                  Path to your movies dir for indexing it.
  --index               Reindex your movies directory.
  -i, --imdb            Sort acc. to IMDB rating.(dec)
  -t, --tomato          Sort acc. to Tomato Rotten rating.(dec)
  -g, --genre           Show moviename & its genre.
  -a, --awards          Show moviename & awards recieved.
  -c, --cast            Show moviename & its cast.
  -d, --director        Show moviename & director name.
  -y, --year            Show moviename & its release year.
  -r, --runtime         Show moviename & its runtime.
  -I, --imdb-rev        Sort acc. to IMDB rating.(inc)
  -T, --tomato-rev      Sort acc. to Tomato Rotten rating.(inc)

"""

import os
import textwrap
import requests
import json
from guessit import guess_file_info
from terminaltables import AsciiTable

from urllib import urlencode

from docopt import docopt

from tqdm import tqdm

OMDB_URL = 'http://www.omdbapi.com/?'

EXT = (".3g2 .3gp .3gp2 .3gpp .60d .ajp .asf .asx .avchd .avi .bik .bix"
       ".box .cam .dat .divx .dmf .dv .dvr-ms .evo .flc .fli .flic .flv"
       ".flx .gvi .gvp .h264 .m1v .m2p .m2ts .m2v .m4e .m4v .mjp .mjpeg"
       ".mjpg .mkv .moov .mov .movhd .movie .movx .mp4 .mpe .mpeg .mpg"
       ".mpv .mpv2 .mxf .nsv .nut .ogg .ogm .omf .ps .qt .ram .rm .rmvb"
       ".swf .ts .vfw .vid .video .viv .vivo .vob .vro .wm .wmv .wmx"
       ".wrap .wvx .wx .x264 .xvid")

EXT = tuple(EXT.split())


def main(docopt_args):
    if docopt_args["PATH"]:
        dir_json = docopt_args["PATH"] + ".json"
        with open("config.py", "w") as inpath:
            inpath.write("PATH = \"" + docopt_args["PATH"] + "\" ")
        scan_dir(docopt_args["PATH"], dir_json)
        print "Run $moviemon"

    elif docopt_args["--index"]:
        try:
            import config
        except ImportError:
            return False
        else:
            val = config.PATH + ".json"
            scan_dir(config.PATH, val)

    elif docopt_args["--imdb"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Imdb"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                              item["Title"], table.column_max_width(0))
                table_data.append([item["Title"], item["imdbRating"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[1]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--tomato"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Tomato"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                              item["Title"], table.column_max_width(0))
                table_data.append([item["Title"], item["tomatoRating"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[1]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--genre"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Genre"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                              item["Title"], table.column_max_width(0))
                table_data.append([item["Title"], item["Genre"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[0]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--awards"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Awards"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                        item["Title"], table.column_max_width(0))
                    if len(item["Awards"]) > table.column_max_width(1):
                        item["Awards"] = textwrap.fill(
                            item["Awards"], table.column_max_width(1))
                elif len(item["Awards"]) > table.column_max_width(1):
                    item["Awards"] = textwrap.fill(
                        item["Awards"], table.column_max_width(1))
                table_data.append([item["Title"], item["Awards"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[0]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--cast"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Cast"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                        item["Title"], table.column_max_width(0))
                    if len(item["Actors"]) > table.column_max_width(1):
                        item["Actors"] = textwrap.fill(
                            item["Actors"], table.column_max_width(1))
                elif len(item["Actors"]) > table.column_max_width(1):
                    item["Actors"] = textwrap.fill(
                        item["Actors"], table.column_max_width(1))
                table_data.append([item["Title"], item["Actors"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[0]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--director"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Director"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                        item["Title"], table.column_max_width(0))
                    if len(item["Director"]) > table.column_max_width(1):
                        item["Director"] = textwrap.fill(
                            item["Director"], table.column_max_width(1))
                elif len(item["Director"]) > table.column_max_width(1):
                    item["Director"] = textwrap.fill(
                        item["Director"], table.column_max_width(1))
                table_data.append([item["Title"], item["Director"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[0]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--year"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Year"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                              item["Title"], table.column_max_width(0))
                table_data.append([item["Title"], item["Released"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[0]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--runtime"]:  # Fix numeric sort
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Runtime"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                              item["Title"], table.column_max_width(0))
                table_data.append([item["Title"], item["Runtime"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[1]))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--imdb-rev"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "IMDB"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                              item["Title"], table.column_max_width(0))
                table_data.append([item["Title"], item["imdbRating"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[1], reverse=True))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    elif docopt_args["--tomato-rev"]:
        try:
            import config
        except ImportError:
            return False
        else:
            table_data = [["Title", "Tomato"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)
            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                              item["Title"], table.column_max_width(0))
                table_data.append([item["Title"], item["tomatoRating"]])
            table_data = (table_data[:1] + sorted(table_data[1:],
                          key=lambda i: i[1], reverse=True))
            table = AsciiTable(table_data)
            table.inner_row_border = True
            print table.table

    else:
        try:
            import config
        except ImportError:
            print "Run $moviemon PATH"
        else:
            table_data = [
                ["Title", "Genre", "Imdb Rating", "Runtime", "Tomato Rating",
                 "Year"]]
            table = AsciiTable(table_data)
            val = config.PATH + ".json"
            with open(val) as inp:
                data = json.load(inp)

            for item in data:
                if len(item["Title"]) > table.column_max_width(0):
                    item["Title"] = textwrap.fill(
                        item["Title"], table.column_max_width(0))
                    if len(item["Genre"]) > table.column_max_width(1):
                        item["Genre"] = textwrap.fill(
                            item["Genre"], table.column_max_width(1))
                elif len(item["Genre"]) > table.column_max_width(1):
                    item["Genre"] = textwrap.fill(
                        item["Genre"], table.column_max_width(1))
                table_data.append([item["Title"], item["Genre"],
                                   item["imdbRating"], item["Runtime"],
                                   item["tomatoRating"], item["Year"]])
            table.inner_row_border = True
            print table.table

movies = []
movie_name = []


def scan_dir(path, dir_json):
    # Preprocess the total files count
    filecounter = 0
    for root, dirs, files in tqdm(os.walk(path)):
        for name in files:
            path = os.path.join(root, name)
            if os.path.getsize(path) > (25*1024*1024):
                ext = os.path.splitext(name)[1]
                if ext in EXT:
                    movie_name.append(name)
                    filecounter += 1

    with tqdm(total=filecounter, leave=True, unit='B',
              unit_scale=True) as pbar:
        for name in movie_name:
            data = get_movie_info(name)
            pbar.update()
            if data is not None and data['Response'] == 'True':
                # if data['Response'] == 'False':  # Movie not found :(
                # TODO: Alert user about non existent movie
                movies.append(data)
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
    args = docopt(__doc__, version='moviemon 1.0')
    main(args)
