# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

sample = str(input())


print(*[(len(list(c)), int(k)) for k, c in groupby(sample)])
