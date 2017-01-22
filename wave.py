import os
import math
import time
import sys

args = sys.argv
nargs = len(args)

if(nargs == 2):
    y = 0
    size = int(args[1])

    while 1:
        a = int(math.sin(y)*size)

        for x in range(0,a+size):
            if(x!=size-1):
                print("."),
            else:
                print("|"),
        
        print('o'),

        for x in range(a+size, size*2):

            if(x != size-2):
                print(" "),
            else:
                print("|"),

        print(" "),

        a = int(math.cos(y)*size)

        for x in range(0,a+size):
            if(x!=size-1):
                print("."),
            else:
                print("|"),
        
        print('o'),

        for x in range(a+size, size*2):

            if(x != size-2):
                print(" "),
            else:
                print("|"),

        print

        y+=0.1
        time.sleep(0.05)

    
else:
    print("Enter a value")
