#!binpython3

import math
import os
import random
import re
import sys

import itertools

if __name__ == '__main__'
    n = int(input().strip())
    num = str(bin(n))[2]
    num_values = [(x[0], len(list(x[1]))) for x in itertools.groupby(num)]
    print(sorted(num_values)[-1][1])
