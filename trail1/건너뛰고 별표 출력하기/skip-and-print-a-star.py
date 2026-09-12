a = int(input())
for i in range(1,a+1):
    for j in range(i):
        print('*',end='')
    print()
    print()
for n in range(a-1,-1,-1):
    for m in range(n):
        print('*',end='')
    print()
    print()
