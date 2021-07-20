#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text_str=[]
for i in range(m):
    text_str += [matrix[j][i] for j in range(n)]

dec_string = "".join(text_str)
fin_txt = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', dec_string)
fin_txt = re.sub('  ', ' ', fin_txt)

print(fin_txt)

