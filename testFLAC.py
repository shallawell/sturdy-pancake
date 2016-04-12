#!/usr/bin/env python3
# Author : shallawell@gmail.com, @shallawell
# A test function to check a if argv contains *.flac
# Filesname: testFLAC.py
# Description:

# ensure PYTHONPATH is set properly
import sys,os,os.path
sys.path.append(os.path.expanduser('/usr/local/lib/python3.4/dist-packages'))

import re

def FLACfileTest():
    # Regex for *.flac
    pattern = r"([a-zA-Z]?\.flac)"
    # Regex for Date
    #pattern = r"([a-zA-Z]+) (\d+)"
    input = str(sys.argv[1])
    #input = "June 24"
#    input = "brian.mp3"  # FALSE condition
    #input = "brian.mp3.flac"  # TRUE condition
    if re.search(pattern, input):
        match = re.search(pattern, input)
        #match = re.search(regex, input)
    # This will print [0, 7), since it matches at the beginning and end of the
    # string
    #print "Match at index %s, %s" % (match.start(), match.end())
    # So this will print "June 24"
    #print "Full match: %s" % (match.group(0))
        print "File ends with FLAC.. runs ok %s" % (match.group(0))
        return 0 # pass
    # So this will print "June"
    #print "Month: %s" % (match.group(1))
    # So this will print "24"
    #print "Day: %s" % (match.group(2))
    else:
    # If re.search() does not match, then None is returned
        print("Error: Must be a FLAC file .. your file was " + sys.argv[1])
        return 1 # fail

# make the file usable as a script as well as an importable module
if __name__ == "__main__":
    import os, fnmatch
    # execute function
    FLACfileTest()

#version info
__version__ = '0.1'