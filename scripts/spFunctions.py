#!/usr/bin/env python3
# Author : shallawell@gmail.com, @shallawell
# Sturdy Pancake App - Transcribe Audio to Text
# Filesname: spFunctions.py
# Description: Collection of functions to use SpeechRecognition modules to convert audio files to text.

import os, fnmatch

def testDIR():
    WORKINGDIR = "/root/speech_recognition/examples"
    #print("WORKINGDIR is " + WORKINGDIR)
    if os.getcwd() == WORKINGDIR:
        #print("CurrentDIR is " + os.getcwd())
        #print("WORKINGDIR is " + WORKINGDIR)
        #print("runs ok")
        return 1
    else:
        #print("CurrentDIR is " + os.getcwd())
        #print("Error: Run this from " + WORKINGDIR)
        return 0

# redefine WORKINGDIR to add a slash to the variable to make it easier down below with filenames and paths. This shoul                 d be improved.
WORKINGDIR = "/root/speech_recognition/examples/"
INPUTLIST_FILE = "/root/speech_recognition/examples/list.txt"

def myCleanUp():
# find and remove old flac files
    print ("Start clean up of old files")
    found_flac_files = (fnmatch.filter(os.listdir(WORKINGDIR), '*.flac'))
# loop through list and delete files
    i=0
    for found_flac_files in found_flac_files:
        i+=1
        os.remove(found_flac_files)
    print ("NBR of FLAC files removed :", +  len(found_flac_files))
# for debug only
#   print(found_flac_files)
# remove old list.txt file
    if os.path.isfile(INPUTLIST_FILE):
        os.remove(INPUTLIST_FILE)
        print("Removed old " + INPUTLIST_FILE)
    else:
        print(INPUTLIST_FILE + " does not exist. Nothing to clean up")
# end myCleanUp()
#Ensure old files removed, run myCleanUp()



# Begin the convert from MP3 to FLAC files
##########################
#import os, fnmatch
# find and create a list of mp3 files
def findMP3files():
    found_mp3_files = (fnmatch.filter(os.listdir(WORKINGDIR), '*.mp3'))
# for debug only
#    print(found_mp3_files)
# set the counter to zero
    i=0
    for found_mp3_file in found_mp3_files:
        i+=1
#    do the conversion
        os.system("avconv -v quiet -i " + found_mp3_file + " -f flac "+ found_mp3_file + ".flac")
#    write the filename to the output file to be used later
        print("Converting " + found_mp3_file + " to FLAC type")
        with open(INPUTLIST_FILE, "a") as text_file:
            text_file.write(found_mp3_file + ".flac" + "\n")


##########################
# Begin to transcribe the audio files
#import os
# set the counter to zero
def transcribeList():
    i=0
#read the file
    f=open(INPUTLIST_FILE,'r')
    print("Starting to Transcribe file list")
#loop through the list and execute the command
    for line in f:
        i+=1
        print("Transcribing " + line)
        os.system("python3 /root/speech_recognition/examples/audio_transcribe.py " + line)
        #print("Done Transcribing " + line)

# make the file usable as a script as well as an importable module
if __name__ == "__main__":
    import os, fnmatch
    # execute function
    spFunctions()

__version__ = '0.1'