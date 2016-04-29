#!/usr/bin/python

from os.path import isfile

logfile="changelog.html"
html_head="<html><head><title>Changelog - Webifier</title><script src='webifier.js'></script></head><body>"
html_pattern="<div onclick='show(this)'><h1><i>[%s] %s</i></h1><span style='visibility:hidden' class='description'>%s</span></div>"

def write_log(name, description, version):
    if not isfile(logfile):
        with open(logfile, "a+") as f:
            f.write(html_head)
    with open(logfile, "a+") as f:
        f.write(html_pattern % (version, name, description))

def main():
    write_log(input("Name : "), input("Description : "), input("Version : "))

if __name__ == "__main__":
    main()
