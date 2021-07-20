#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    
    assert 1<=n<=100, "n not in range"
    assert all(ele >= 1 and ele <= 100 for ele in ar), "ar elements not in range"
    assert len(ar)==n, "n and length of ar not equal"
    # Write your code here
    
    result = 0
    for item in Counter(ar).items():
        result += item[1]//2

    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
