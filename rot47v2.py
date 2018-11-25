#!/usr/bin/python

import sys

def rot47(sClr):

    i = 0
    iTemp= 0

    while i < len(sClr):
        iTemp= ord(sClr[i])
        
        if iTemp > 32 and iTemp < 127:
            iTemp = ((iTemp -33) + 47) %94
            sys.stdout.write(chr(iTemp + 33))
                 
        else:
            sys.stdout.write(chr(iTemp))  
    
        i += 1
    print "\n"

sMsg = raw_input('Message: ')
rot47(sMsg)

# Python 2.7.6


