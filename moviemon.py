"""moviemon.

Usage:
  moviemon.py -h
  moviemon.py --version
  moviemon.py [-m | -i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]

Options:
  -h --help     Show this screen.
  --version     Show version.
  -m                    Display basic info about all movies.
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
import requests
import json
from guessit import guess_file_info

from urllib import urlencode

from config import PATHS

from prettytable import PrettyTable

from docopt import docopt


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
    if docopt_args["-m"]:
        print basic_table.get_string(sortby="Title")
    elif docopt_args["--imdb"]:
        print imdb_table.get_string(sortby="Imdb Rating", reversesort=True)
    elif docopt_args["--tomato"]:
        print tomato_table.get_string(sortby="Tomato Rating", reversesort=True)
    elif docopt_args["--genre"]:
        print genre_table.get_string(sortby="Title")
    elif docopt_args["--awards"]:
        print awards_table.get_string(sortby="Title")
    elif docopt_args["--cast"]:
        print cast_table.get_string(sortby="Title")
    elif docopt_args["--director"]:
        print direct_table.get_string(sortby="Title")
    elif docopt_args["--year"]:
        print release_table.get_string(sortby="Title")
    elif docopt_args["--runtime"]:
        print runtime_table.get_string(sortby="Title")
    elif docopt_args["--imdb-rev"]:
        print imdb_table.get_string(sortby="Imdb Rating")
    elif docopt_args["--tomato-rev"]:
        print tomato_table.get_string(sortby="Tomato Rating")
    else:
        print "Use -h for help"


def scan_dir(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            path = os.path.join(root, name)
            # Validation for file size
            if os.path.getsize(path) > (25*1024*1024):
                ext = os.path.splitext(name)[1]
                if ext in EXT:
                    get_movie_info(name)


def get_movie_info(name):
    """Find movie information"""
    movie_info = guess_file_info(name)
    if movie_info['type'] == "movie":
        if 'year' in movie_info:
            omdb(movie_info['title'], movie_info['year'])
        else:
            omdb(movie_info['title'], None)


def omdb(title, year):
    """ Fetch data from OMDB API. """
    params = {'t': title.encode('ascii', 'ignore'),
              'plot': 'full',
              'type': 'movie',
              'tomatoes': 'true'}

    if year:
        params['y'] = year

    url = OMDB_URL + urlencode(params)

    data = requests.get(url)

    source = json.loads(data.text)

    if source['Response'] == 'True':  # Movie not found :(
        with open(dir_json, "a") as out:
            json.dump(source, out, indent=2)
            # `,` is a hack for validating JSON, ask duffer
            out.write(",\n")


if __name__ == '__main__':
    for path in PATHS:
        dir_json = path + ".json"
        # if os.path.exists(dir_json):
        #     try:
        #         os.remove(dir_json)
        #     except OSError:
        #         pass
        # with open(dir_json, "w") as out:   # Hack for validating JSON, ask duffer
        #     out.write("[")
        # scan_dir(path)
        # with open(dir_json, "a") as out:   # Hack for validating JSON, ask duffer
        #     out.write("]")

    with open(dir_json) as inp:
        data = json.load(inp)

    # snippet for -m
    basic_table = PrettyTable(["Title", "Genre", "Imdb Rating", "Runtime", "Tomato Rating", "Year"])
    basic_table.align["Title"] = "l"
    basic_table.align["Genre"] = "l"

    # snippet for sorting acc to imdb rating `-i | -I`
    imdb_table = PrettyTable(["Title", "Imdb Rating"])
    imdb_table.align["Title"] = "l"

    # snippet for sorting acc to tomato rating `-t | -T`
    tomato_table = PrettyTable(["Title", "Tomato Rating"])
    tomato_table.align["Title"] = "l"

    # snippet for movie & genre   `-g`
    genre_table = PrettyTable(["Title", "Genre"])
    genre_table.align["Title"] = "l"
    genre_table.align["Genre"] = "l"

    # snippet for title & awards  `-a`
    awards_table = PrettyTable(["Title", "Awards"])
    awards_table.align["Title"] = "l"
    awards_table.align["Awards"] = "l"

    # snippet for movie & cast  `-c`
    cast_table = PrettyTable(["Title", "Cast"])
    cast_table.align["Title"] = "l"
    cast_table.align["Cast"] = "l"

    # snippet for movie & director  `-d`
    direct_table = PrettyTable(["Title", "Director"])
    direct_table.align["Title"] = "l"
    direct_table.align["Director"] = "l"

    # snippet for movie & release date  `-y`
    release_table = PrettyTable(["Title", "Released"])
    release_table.align["Title"] = "l"

    # snippet for runtime  `-r`
    runtime_table = PrettyTable(["Title", "Runtime"])
    runtime_table.align["Title"] = "l"

    for item in data:
        if len(item["Title"].split()) <= 10:  # So that the table doesn't get fucked
            basic_table.add_row([item["Title"], item["Genre"],
                                 item["imdbRating"], item["Runtime"],
                                 item["tomatoRating"], item["Year"]])
            imdb_table.add_row([item["Title"], item["imdbRating"]])
            tomato_table.add_row([item["Title"], item["tomatoRating"]])
            awards_table.add_row([item["Title"], item["Awards"]])
            runtime_table.add_row([item["Title"], item["Runtime"]])
            cast_table.add_row([item["Title"], item["Actors"]])
            direct_table.add_row([item["Title"], item["Director"]])
            release_table.add_row([item["Title"], item["Released"]])
            genre_table.add_row([item["Title"], item["Genre"]])

    args = docopt(__doc__, version='moviemon 1.0')
    main(args)
