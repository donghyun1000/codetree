a = int(input())
for i in range(a):
    for j in range(a-i):
        print('*', end='')
    print(' '*(2*i),end='')
    for j in range(a-i):
        print('*', end='')
    print()