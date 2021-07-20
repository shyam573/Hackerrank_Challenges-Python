# Enter your code here. Read input from STDIN. Print output to STDOUT


def find_idea(arrays):
    main_ar,A,B = arrays
    A_count = B_count = 0
    A=set(A)
    B=set(B)
    for elem in main_ar:
        if elem in A:
            A_count+=1
        elif elem in B:
            B_count+=1
        else:
            pass

    return A_count-B_count

n,m = list(map(int,input().rstrip().split()))
arrays = []
for _ in range(3):
    arrays.append(input().split())
    
result = find_idea(arrays)
print(result)
