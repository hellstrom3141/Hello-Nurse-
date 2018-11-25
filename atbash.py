#!/usr/bin/python

import sys

for line in sys.stdin:

    i = 0
    iTemp= 0

    while i < len(line):
        iTemp= ord(str.upper(line[i]))
    
        if iTemp > 64 and iTemp < 91:
            iTemp = 90 - (iTemp % 65)
            sys.stdout.write(chr(iTemp))
              
        else:
            sys.stdout.write(chr(iTemp))  
    
        i += 1
    





# Python 2.7.6


