#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    clock_list = s[:-2].split(":")
    if s[-2:]=="AM":
        if clock_list[0]=="12":
            clock_list[0]="00"
        else:
            pass
    else:
        if clock_list[0]=="12":
            pass
        else:
            clock_list[0]=str(int(clock_list[0])+12)
    
    return ":".join(clock_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
