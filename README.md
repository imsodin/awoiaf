Overview
========

This project contains the code base to extract data from the wiki portal http://awoiaf.westeros.org.

Repo structure
==============

 |  
 |-scr - main scripts (python)   
 |-etc - configration  
 |-data - downloaded data   


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
* 
```
$ easy_install nltk beautifulsoup4
```
or
````
$ pip install nltk beautifulsoup4
```

Configuration
-------------

Change etc/awoiafrc.default:2 to reflect the root installation dir 

```
[Folders]
dir=/path/to/awoiaf
rootdir: %(dir)s
datadir: %(dir)s/Data
visdir: %(dir)s/vis
```





