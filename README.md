# moviemon

**A Python Application that displays all the information about all your movies in the command line.**

(Bada wala GIF)


## Installation

### Using [pip](https://pypi.python.org/pypi/pip/)

`$ pip install moviemon`

You can also use [pipsi](https://github.com/mitsuhiko/pipsi) to install -

`$ pipsi install moviemon`


### Get the latest build from the Source

* Clone the repo git clone https://github.com/iCHAIT/moviemon
* Run python setup.py install


### Dependencies

* [guessit](https://github.com/guessit-io/guessit)
* [terminaltables](https://github.com/Robpol86/terminaltables)
* [docopt](https://github.com/docopt/docopt)
* [tqdm](https://github.com/tqdm/tqdm)
* [colorama](https://github.com/tartley/colorama)


### Usage:
```sh
  moviemon.py PATH
  moviemon [-i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
  moviemon -h | --help
  moviemon --version
```

### Options:
```sh
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
```

### Examples -

Display basic info about all your movies.

`$ moviemon -m`

[**DEMO**]()

Display all movies sorted according to their [IMDB](http://www.imdb.com/) ratings.

`$ moviemon -i`

[**DEMO**]()

Display all movies sorted according to their [Tomato Rotten](http://www.rottentomatoes.com/) ratings.

`$ moviemon -t`

[**DEMO**]()

Display all movies with their Genres.

`$ moviemon -g`

[**DEMO**]()

Display all movies with the awards they have recieved.

`$ moviemon -a`

[**DEMO**]()

Display all movies with their cast.

`$ moviemon -c`

[**DEMO**]()

Display all movies with their director(s).

`$ moviemon -d`

[**DEMO**]()

Display all movies with their release date.

`$ moviemon -y`

[**DEMO**]()

Display all movies sorted according to their [IMDB](http://www.imdb.com/) ratings.(inc)

`$ moviemon -I`

[**DEMO**]()

Display all movies sorted according to their [Tomato Rotten](http://www.rottentomatoes.com/) ratings.(inc)

`$ moviemon -T`

[**DEMO**]()


### Stretch Goals

* Use MongoDB to store data instead of storing json data in file.
* Run a cron job to detect if the directory containg movies has been modified, if it has been modified then reindex the directory for accomdating new or deleted movies.
* As mentioned by [@dufferzafar](https://github.com/dufferzafar) this can seriously become a movie database 'tagger' like [Picard](https://picard.musicbrainz.org/).


### Shout-out

Big thanks to [@dufferzafar](https://github.com/dufferzafar) for his [awesome work](https://github.com/dufferzafar/what-to-watch).


### Contribute

Found a bug or want to suggest a new feature? Report it by opening an issue. Feel free to send a pull request for any improvements or feature requests ;)


### License

MIT © [Chaitanya Gupta](https://github.com/iCHAIT)
