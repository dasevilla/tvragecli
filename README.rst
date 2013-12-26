==========
TVRage CLI
==========

::

    usage: tvrage [--version] [-v] [-q] [-h] [--debug]

    Command line client for TV Rage

    optional arguments:
      --version      show program's version number and exit
      -v, --verbose  Increase verbosity of output. Can be repeated.
      -q, --quiet    suppress output except warnings and errors
      -h, --help     show this help message and exit
      --debug        show tracebacks on errors

    Commands:
      epinfo         episode details
      eplist         list episodes
      help           print detailed help for another command
      search         search for tv shows
      showinfo       tv show details


Developing
==========

::

  $ mkvirtualenv tvragecli
  $ git clone git://github.com/dasevilla/tvragecli.git tvragecli
  $ cd tvragecli
  $ pip install -r requirements.txt
  $ python setup.py develop
  $ tox # Test source using pep8, pyflakes
