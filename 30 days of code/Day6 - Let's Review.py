# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
strings = []
for _ in range(n):
    strings.append(input())
    
for string in strings:
    even = "".join([string[i] for i in range(len(string)) if i%2==0])
    odd = "".join([string[i] for i in range(len(string)) if i%2!=0])
    print(even, odd)
