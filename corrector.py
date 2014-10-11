# -*- coding: utf-8 -*-
'''
This scripts corrects a given HTML file for umlaute.
All special letters will replaced by html conform
escape sequences.

@author: nick m
'''

import sys, os


if __name__ == '__main__':

  # Demonstrate the usage
  if not len(sys.argv) == 2:
    print "usage: python corrector.py <HTML-FILE>"
    sys.exit(-1)

  # Get commandline argument for the file
  file = sys.argv[1]

  # Just an existing file is good enougth
  if os.path.isfile(file):

    # Open up and read the data
    f = open(file, "r")
    data = f.read()
    f.close()

    # Replace them all
    data = data.decode('utf-8')
    data = data.replace(u'ü', "&uuml;")
    data = data.replace(u'Ü', "&Uuml;")
    data = data.replace(u'ä', "&auml;")
    data = data.replace(u'Ä', "&auml;")
    data = data.replace(u'ö', "&ouml;")
    data = data.replace(u'Ö', "&Ouml;")
    data = data.replace(u'ß', "&szlig;")

    # Override the old file with new data
    f = open(file, "w")
    f.write(data.encode("utf8"))
    f.close()

  else:
    print "file {} not exists.".format(file)
