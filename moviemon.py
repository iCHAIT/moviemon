import os
import urllib2

from guessit import guess_file_info

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

movies = []


def scan_dir(path):
    for root, dirs, files in os.walk(path):
            for name in files:
                path = os.path.join(root, name)
                if os.path.getsize(path) > (25*1024*1024):
                    ext = os.path.splitext(name)[1]
                    if ext in EXT:
                        print name
                        get_movie_info(name)
                        print "\n"
                        # movies.append(movie_name)

# print movies


# def omdb():
#   """ Fetch data from OMDB API. """
#     url = OMDB_URL +


def get_movie_info(name):
    """Find movie information"""
    movie_name = guess_file_info(name)
    print movie_name


if __name__ == '__main__':
    for path in PATHS:
        scan_dir(path)
