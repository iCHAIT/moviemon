# Movie Maniac


A Command-Line Python Application to display information about movies on your PC from the CLI !

Scans folders for movies, and fetches their data from the OMDB API and displays it in CLI.
 
### Using [pip]()

pip install moviemon

### Get the latest build from the Source

* Clone the repo git clone https://github.com/iCHAIT/movie-maniac
* 


### Options

-h, --help          show this help message and exit
-R README, --readme README
                    Get the raw version of the repository readme file from repo link URL



### Usage 

### Demos

### METHODODLGY -

* Provide switches option for all your movies by their -
        * IMDB ratings
        * roten tomatoes rating
        * runtime/length
        * release year (recent movie appears on top)
        * genre
        * director
        * actors
        * Awards


### TODO

- [ ] Use PrettyTable to tabulate the output in CLI
- [ ] Start off with switches
- [ ] Learn about json.dump() json.dumps() json.load() json.loads()


### Known Issues

* Valid JSON not getting written into file, currently using hacks by explicitly writing `[`, `]` and truncating a comma at last.

* If length of movie title is > 10 then table gets fucked up.

* Runtime column not getting sorted (just considers the first number for sorting)
