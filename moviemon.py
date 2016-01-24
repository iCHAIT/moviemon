import os
import requests
import json
from guessit import guess_file_info

from urllib import urlencode

from config import PATHS

from prettytable import PrettyTable

OMDB_URL = 'http://www.omdbapi.com/?'

EXT = (".3g2 .3gp .3gp2 .3gpp .60d .ajp .asf .asx .avchd .avi .bik .bix"
       ".box .cam .dat .divx .dmf .dv .dvr-ms .evo .flc .fli .flic .flv"
       ".flx .gvi .gvp .h264 .m1v .m2p .m2ts .m2v .m4e .m4v .mjp .mjpeg"
       ".mjpg .mkv .moov .mov .movhd .movie .movx .mp4 .mpe .mpeg .mpg"
       ".mpv .mpv2 .mxf .nsv .nut .ogg .ogm .omf .ps .qt .ram .rm .rmvb"
       ".swf .ts .vfw .vid .video .viv .vivo .vob .vro .wm .wmv .wmx"
       ".wrap .wvx .wx .x264 .xvid")

EXT = tuple(EXT.split())


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
    # what if I have TV shows in that folder?
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

    x = PrettyTable(["Title", "Genre", "imdbRating", "Runtime", "tomatoRating", "Year"])
    x.align["Title"] = "l"
    x.align["Genre"] = "l"

    for item in data:
        if len(item["Title"].split()) <= 10:  # So that the table doesn't get fucked
            x.add_row([item["Title"], item["Genre"],item["imdbRating"], item["Runtime"],item["tomatoRating"], item["Year"]])

    print x

'''
Note - Learn about json.dump() json.dumps() json.load() json.loads()
'''
