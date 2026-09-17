a = int(input())
for i in range(a):
    for j in range(i):
        print(' ',end=' ')
    for k in range(a-i,0,-1):
        print(k, end=' ')
    print()