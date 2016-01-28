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
* prettytable
* docopt


### Usage:
```sh
  moviemon -h
  moviemon --version
  moviemon [-m | -i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
```

### Options:
```sh
  -h --help     Show this screen.
  --version     Show version.
  -m                    Display basic info about all movies.
  -i, --imdb            Sort acc. to IMDB rating.(dec)
  -t, --tomato          Sort acc. to Tomato Rotten rating.(dec)
  -g, --genre           Show moviename and its genre.
  -a, --awards          Show moviename and awards recieved.
  -c, --cast            Show moviename and its cast.
  -d, --director        Show moviename and director name.
  -y, --year            Show moviename and its release year.
  -r, --runtime         Show moviename and its runtime
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

- [ ] When path is given via CLI make sure to write it in a config file, and overwrite this path when a different path is supplied.

- [ ] Get the char length of user's terminal and display column's acc.

- [ ] Use prettytable numeric sort for sorting runtime

- [ ] Use infinite progress bar

- [ ] Cases for running moviemon as discussed with duffer


### Contribute

Feel free to open issues or send a pull request for any bugs or feature requests :)


### License

MIT © [Chaitanya Gupta](https://github.com/iCHAIT)
