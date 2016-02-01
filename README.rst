moviemon
========

**A Python Application that displays all the information about all your movies in the command line.**


Installation
============

Using ``pip``
-------------

.. code:: sh

   $ pip install moviemon

You can also use `pipsi <https://github.com/mitsuhiko/pipsi>`__ to install -

.. code:: sh

  $ pipsi install moviemon


Get the latest build from the Source
------------------------------------

- Clone the repo

.. code:: sh

    git clone https://github.com/iCHAIT/moviemon

- Run

.. code:: sh

    $ python setup.py install


Dependencies
============

- `guessit <https://github.com/guessit-io/guessit>`__
- `terminaltables <https://github.com/Robpol86/terminaltables>`__
- `docopt <https://github.com/docopt/docopt>`__
- `tqdm <https://github.com/tqdm/tqdm>`__
- `colorama <https://github.com/tartley/colorama>`__


Usage:
======

.. code:: sh

  moviemon.py PATH
  moviemon [-i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
  moviemon -h | --help
  moviemon --version


Options:
========

.. code:: sh

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


Examples -
==========

Display basic info about all your movies.

``$ moviemon -m``

Display all movies sorted according to their IMDB ratings.

``$ moviemon -i``

Display all movies sorted according to their Tomato Rotten ratings.

``$ moviemon -t``

Display all movies with their Genres.

``$ moviemon -g``

Display all movies with the awards they have recieved.

``$ moviemon -a``

Display all movies with their cast.

``$ moviemon -c``

Display all movies with their director(s).

``$ moviemon -d``

Display all movies with their release date.

``$ moviemon -y``

Display all movies sorted according to their IMDB ratings (inc).

``$ moviemon -I``

Display all movies sorted according to their Tomato Rotten ratings (inc).

``$ moviemon -T``


Contribute
==========

Found a bug or want to suggest a new feature? Report it by opening an issue. Feel free to send a pull request for any improvements or feature requests.
