# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys


n = int(input())
dict_val={}
for _ in range(n):
    inp = input().split()
    dict_val.update({inp[0]:inp[1]})
    
queries=[]
for query in sys.stdin:
    queries.append(query.rstrip())
    
for query in queries:
    if query in dict_val:
        print(query+"="+dict_val[query])
    else:
        print("Not found")
