a = int(input())

for i in range(1,2*a):
    if i <a+1:
        for _ in range(a-i):
            print('',end=' ')
        for _ in range(i):
            print('*',end=' ')
        print()
    else:
        for _ in range(i-a):
            print('',end=' ')
        for _ in range(2*a-i):
            print('*',end=' ')
        print()