#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    
    sorted_arr = sorted(arr)
    
    if arr == sorted_arr:
        print("yes")
        sys.exit()
        
    mismatch = [i for i in range(len(arr)) if arr[i]!=sorted_arr[i]]
    l = min(mismatch)
    r = max(mismatch)

    if len(mismatch)<=2:
        print("yes")
        print("swap " + str(l+1) +" "+ str(r+1))
        sys.exit()
    else:
        if arr[l:r+1][::-1]==sorted_arr[l:r+1]:
            print("yes")
            print("reverse " + str(l+1) +" " + str(r+1))
            sys.exit()
        else:
            print("no")
            sys.exit()

        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
