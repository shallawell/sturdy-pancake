
from spFunctions import testDIR, myCleanUp, findMP3files, transcribeList

print('Version', mymodule.__version__)

#execute function
if testDIR() == 0:
    exit()
else:
    myCleanUp()
    findMP3files()
    transcribeList()
##########################
#  Clean up files and leave only originals in place + trans.out (the output file)
# call my function
    myCleanUp()

__version__ = '0.1'