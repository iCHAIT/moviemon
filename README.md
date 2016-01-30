# moviemon

A Command-Line Python Application to display information about movies on your PC from the CLI.

Scans folders for movies, and fetches their data from the OMDB API and displays it in CLI.

(Bada wala GIF)


### Using [pip](https://pypi.python.org/pypi/pip/)

`$ pip install moviemon`

You can also use [pipsi](https://github.com/mitsuhiko/pipsi) to install -

`$ pipsi install moviemon`


### Get the latest build from the Source

* Clone the repo git clone https://github.com/iCHAIT/moviemon
* Run python setup.py install


### Dependencies

* guessit
* terminaltables
* docopt
* tqdm
* colorama


### Usage:
```sh
  moviemon.py PATH
  moviemon.py --index
  moviemon.py [-i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
  moviemon.py -h | --help
  moviemon.py --version
```

### Options:
```sh
  -h, --help            Show this screen.
  -v, --version         Show version.
  PATH                  Path to your movies dir.
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

Display all movies sorted according to their [IMDB](http://www.imdb.com/) ratings(inc).

`$ moviemon -I`

[**DEMO**]()

Display all movies sorted according to their [Tomato Rotten](http://www.rottentomatoes.com/) ratings(inc).

`$ moviemon -T`

[**DEMO**]()


### TODO

- [ ] Use numeric sort for sorting runtime, add reverse runtime func.
- [ ] Package with pip
- [ ] asciinema
- [ ] Github page


### Shout-out

Big thanks to [@dufferzafar](https://github.com/dufferzafar) for his [awesome work](https://github.com/dufferzafar/what-to-watch).


### Contribute

Found a bug or want to suggest a new feature? Report it by opening issues. Feel free to send a pull request for the same ;)


### License

MIT © [Chaitanya Gupta](https://github.com/iCHAIT)
