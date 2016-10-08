#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import argparse

# Default values
########################################################################################

template = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{}</title>
        <meta charset="utf-8">
        <style>
            {}
            .remark-code, .remark-inline-code {{ font-family: 'Ubuntu Mono'; }}
        </style>
    </head>
    <body>
        <textarea id="source">
{}

{}
        </textarea>
        <script src="https://gnab.github.io/remark/downloads/remark-latest.min.js"></script>
        <script>
            var slideshow = remark.create();
        </script>
    </body>
</html>
'''

css = '''
  @import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
  @import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
  @import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);

  body { font-family: 'Yanone Kaffeesatz'; }
  h1, h2, h3 {
    font-family: 'Yanone Kaffeesatz';
    font-weight: normal;
  }
'''

settings = "class: center, middle"
separators = ["#", "##", "###", "####"]
outputFile = "out.html"

# Utils
########################################################################################

def getFileContent(filePath):
    with open(filePath, 'r') as content_file:
        content = content_file.read()
    return(content)


# Main routine
########################################################################################

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # Required input file
    parser.add_argument("markdownfile", help="expects the path to the markdown file")

    # Optional arguments
    parser.add_argument("--css", help="path to a custom css file", action="store")
    parser.add_argument("--settings", help="remarkjs settings (Default: 'class: center, middle'", action="store")
    parser.add_argument("--slidesep", help="defines the string for separate slides. Expects a comma separated list (Default: '#,##,###,####')", action="store")
    parser.add_argument("--output", help="defines the output file (Default: ./out.html)", action="store")

    args = parser.parse_args()
    mdFile = args.markdownfile

    # Override user defined settings
    if args.settings:       settings = args.settings
    if args.css:            css = getFileContent(args.css)
    if args.slidesep:       separators = args.slidesep.replace(" ", "").split(",")
    if args.output:         outputFile = args.output

    # Read file
    mdContent = getFileContent(mdFile)

    # Find separators and create the necessary shape
    parsedContent = ""
    for line in mdContent.split('\n'):
        for element in separators:
            if line.startswith(element+" "):
                parsedContent += "---\n"

        parsedContent += line + "\n";

    # Write file
    target = open(outputFile, 'w')
    target.write(template.format("Presentation", css, settings, parsedContent))
    target.close()
