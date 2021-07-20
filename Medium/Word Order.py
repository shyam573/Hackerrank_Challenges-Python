# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

def count_words(inp):
    result = Counter(inp)
    print(len(result))
    print(" ".join([str(i) for i in result.values()]))
     
words=[]
num = int(input())
for _ in range(num):
    words.append(input())
 
count_words(words)
