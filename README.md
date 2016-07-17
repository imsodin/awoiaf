Overview
========

This project contains the code base to extract data from the wiki portal http://awoiaf.westeros.org.

![Iron Throne](https://rostlab.org/owiki/images/d/d7/Got21_400.jpg)

Repo structure
==============
```
 |
 |-src - main code base (python)
 |--lib - application modules
 |--sge - scripts to run jobs in parallel on a compute cluster
 |-Data - downloaded data
```

Quick Start
===========

Prerequisites
-------------

* easy_install or pip - package managers for python

Easy setup
------------

To download the dependencies: set the correct PYTHONPATH, run `. ./build.sh` from the root directory of this repository. NB: The first . is necessary to export the PYTHONPATH to your current bash session.

**Important**: it is necessary to export the PYTONPATH every time you wish to run these tools. To do so you can either run the build script every time, or jump to the configuration section below.

Alternatively follow the next steps:

Dependencies
------------

* nltk - NLTK is a leading platform for building Python programs to work with human language data.
* BeautifulSoup - Beautiful Soup is a Python library for pulling data out of HTML and XML files.
* requests - requests is a Python module for sending HTTP requests.
* Punkt Sentence Tokenizer and Perceptron modules for nltk.
```
$ easy_install nltk beautifulsoup4 requests
```
or
````
$ pip install nltk beautifulsoup4 requests
```

Next execute
```
$ python -m nltk.downloader punkt averaged_perceptron_tagger
```

*** NOTE ***: you may need to setup PYTHONPATH to include the path of installed modules if those were installed into non-default locations (for instance if you installed it into your user space).

Configuration
-------------

You will need to set up the PYTHONPATH to reference the lib folder

```
# in bash
AWOIAF_ROOT=/path/to/awoiaf/
export PYTHONPATH="${PYTHONPATH}:${AWOIAF_ROOT}/src/lib"
```

Hint
----
The scrtips in the scr folder are used as the main drivers that build the data repository. You can look at those scripts as an entry point into the code. Here is a bried description for each script:

- mineCharDetails.py  - handles Ice and Fire characters' data. scripts can be used to:
  1. `python mineCharDetails -l` obtain a list of charchater names
  2. `python mineCharDetails -c "Some One"` extract data from wiki entries dedicated to character `Some One`.

- mineHousesDetails.py  - handles data related to the great houses of Westeros. scripts can be used to:
  1. `python mineHousesDetails -l` obtain a list of all the houses names mentioned in the AWOIAF wiki
  2. `python mineHousesDetails -s "House Name"`extracts data from wiki pages dedicated to `House Name`.


Look at the scripts in the scr folder to see how the modules in this app can be used and

Running multiple jobs in parallel
=================================

As this project deals with processing 1000s of wiki pages it would make sense to use parallel processing to speed things up. If you have access to a compute cluster and to the sonofgrid scheduling system (formerly called SGE) then check the folder scr/sge for scripts and documentation on how to run paralllel jobs. If you want to schedule jobs using a different system (e.g. Hadoop YARN) then you will have to figure out how to do this yourself.
