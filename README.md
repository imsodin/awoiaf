Overview
========

This project contains the code base to extract data from the wiki portal http://awoiaf.westeros.org.

![Iron Throne](https://rostlab.org/owiki/images/d/d7/Got21_400.jpg)

Repo structure
==============
```
 |
 |-scr - main driver scripts (python)
 |--lib - application modules
 |--sge - scripts to run jobs in parallel on a compute cluster  
 |-etc - configration
 |-Data - downloaded data
```

Quick Start
===========

Prerequisites
-------------

* MongoDB - NoSQL document database
* easy_install or pip - package managers for python

Dependencies
------------

* nltk -NLTK is a leading platform for building Python programs to work with human language data.
* BeautifulSoup - Beautiful Soup is a Python library for pulling data out of HTML and XML files.
```
$ easy_install nltk beautifulsoup4
```
or
````
$ pip install nltk beautifulsoup4
```

NOTE: you may need to setup PYTHONPATH to include the path of installed modules if those were installed into non-default locations (for instance if you installed it into your user space).

Configuration
-------------

You will need to set up the PYTHONPATH to refeerence the lib folder

```
# in bash
AWOIAF_ROOT=/path/to/awoiaf/
export PYTHONPATH="${PYTHONPATH}:${AWOIAF_ROOT}/scr/lib"
```

Change etc/awoiafrc.default:2 to reflect the root installation dir

```
[Folders]
dir=/path/to/awoiaf
rootdir: %(dir)s
datadir: %(dir)s/Data
visdir: %(dir)s/vis
```

hint
----

Look at the scripts in the scr folder to see how the modules in this app can be used and to build your data repository. 

Running multiple jobs in parallel
=================================

As this project deals with processing 1000s of wiki pages it would make sense to use parallel processing to speed things up. If you have access to a compute cluster and to the sonofgrid scheduling system (formerly called SGE) then check the folder scr/sge for scripts and docusmentation on how to run paralllel jobs. If you want to schedule jobs using a different system (e.g. Hadoop YARN) then you will have to figure out how to do this yourself. 
