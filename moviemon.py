import os
import urllib2

from guessit import guess_file_info

from urllib import urlencode

from config import PATHS

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
                if os.path.getsize(path) > (25*1024*1024):    # split this into separate func.
                    ext = os.path.splitext(name)[1]
                    if ext in EXT:
                        get_movie_info(name)
                        print "\n"


def omdb(title, year):
    """ Fetch data from OMDB API. """
    params = {'t': title.encode('ascii', 'ignore'),
              'plot': 'full',
              'type': 'movie',
              'tomatoes': 'true'}

    if year:
        params['y'] = year

    url = OMDB_URL + urlencode(params)
    print url


def get_movie_info(name):
    """Find movie information"""
    movie_info = guess_file_info(name)
    if movie_info['type'] == "movie":    # what if I have TV shows in that folder?
        if movie_info.has_key('year'):
            omdb(movie_info['title'], movie_info['year'])
        else:
            omdb(movie_info['title'], None)


if __name__ == '__main__':
    for path in PATHS:
        scan_dir(path)
