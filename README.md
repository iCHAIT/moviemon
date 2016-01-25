# Movie Maniac

A Command-Line Python Application to display information about movies on your PC from the CLI.

Scans folders for movies, and fetches their data from the OMDB API and displays it in CLI.

(Bada wala GIF)

### Using [pip]()

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
  moviemon.py -h
  moviemon.py --version
  moviemon.py [-m | -i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
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

### Example -

Display basic info about all your movies.

`$ py moviemon.py -m`

[**DEMO**]()

Display all movies sorted according to their IMDB ratings.

`$ py moviemon -i`

[**DEMO**]()

Display all movies sorted according to their Tomato Rotten ratings.

`$ py moviemon -t`

[**DEMO**]()

Display all movies with their Genres.

`$ py moviemon -g`

[**DEMO**]()

Display all movies with the awards they have recieved.

`$ py moviemon -a`

[**DEMO**]()

Display all movies with their cast.

`$ py moviemon -c`

[**DEMO**]()

Display all movies with their director(s).

`$ py moviemon -d`

[**DEMO**]()

Display all movies with their release date.

`$ py moviemon -y`

[**DEMO**]()

Display all movies sorted according to their IMDB ratings(increasing).

`$ py moviemon -I`

[**DEMO**]()

Display all movies sorted according to their Tomato Rotten ratings(increasing).

`$ py moviemon -T`

[**DEMO**]()


### TODO

- [ ] Learn about json.dump() json.dumps() json.load() json.loads()


### Known Issues

* Should I store JSON in a fil, or should we fetch the data on the fly?

* Valid JSON not getting written into file, currently using hacks by explicitly writing `[`, `]` and truncating a comma at last.

* If length of movie title is > 10 then table gets fucked up.

* Runtime column not getting sorted (just considers the first number for sorting)

* What about movies that gets guessed incorrectly, eg Oceans Eleven resulting in response="False"


### Contribute

Want to report bugs, make a feature requests, improve something feel free to open issue or send a pull request.


### License

MIT © [Chaitanya Gupta](https://github.com/iCHAIT)
