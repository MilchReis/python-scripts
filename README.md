python-scripts
=============

Small python snippets for small problems.

## markdown2slides.py ##
This small script converts a markdown text file into a html5 web presentation based on remarkjs. The main advantage and reason for this script is the possibilty for ignoring the remarkjs slider separators. The script will add the necessary separators by definition. In that way each markdown file can convert into slides without chaning the markdown resouce file.

```
usage: markdown2slides.py [-h] [--css CSS] [--settings SETTINGS]
                          [--slidesep SLIDESEP] [--output OUTPUT] markdownfile

positional arguments:
  markdownfile         expects the path to the markdown file

optional arguments:
  -h, --help           show this help message and exit
  --css CSS            path to a custom css file
  --settings SETTINGS  remarkjs settings (Default: 'class: center, middle'
  --slidesep SLIDESEP  defines the string for separate slides. Expects a comma 
                       separated list (Default: '#,##,###,####')
  --output OUTPUT      defines the output file (Default: ./out.html)
```

## communication.py ##
The little library provides a more comfortable access to the information exchange over sockets. The including threading realises a parallel processing for incoming informations. Also the snippet can be used for interprocess communication.

See the usage as an example inside the file.

## corrector.py ##
Replaces umlaute , like ü, ä, ö and ß in a HTML conform escape-sequence.

`usage: python corrector.py <HTML-FILE>`


## loc.py ##
Counts the lines of code for a python project. Works for counting including and excluding the comments.
WALK and LOC routine is from the internet. Unfortunately I lost the url. Use it for a directory of the project and the routine will searches recursive the directory hierarchy.

`usage: python loc.py <PATH>`
