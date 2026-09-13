a = int(input())
for i in range(a*2-1):
    if i<a:
        for j in range(i):
            print(' ',end=' ')
        for j in range(2*a-2*i-1):
            print('*',end=' ')
        print()
    else:
        for j in range(2*a-2-i):
            print(' ',end=' ')
        for j in range(2*i-2*a+3):
            print('*',end=' ')
        print()