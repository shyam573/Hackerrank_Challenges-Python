#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_sum = sum([1 for i in arr if i>0])
    neg_sum = sum([1 for i in arr if i<0])
    zero_sum = sum([1 for i in arr if i==0])
    n = len(arr)
    print(pos_sum/n)
    print(neg_sum/n)
    print(zero_sum/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
