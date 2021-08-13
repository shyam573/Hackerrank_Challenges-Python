#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = tip_percent/100.0 * meal_cost
    tax = tax_percent/100.0 * meal_cost
    print(int(round(meal_cost+tip+tax)))

if __name__ == '__main__':
    meal_cost = float(raw_input().strip())

    tip_percent = int(raw_input().strip())

    tax_percent = int(raw_input().strip())

    solve(meal_cost, tip_percent, tax_percent)