python-scripts
=============

Small python snippets for small problems.

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
