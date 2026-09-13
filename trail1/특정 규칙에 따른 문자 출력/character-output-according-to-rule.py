a = int(input())

for i in range(2*a-1):
    if i<a:
        for j in range(1,a-i):
            print(' ', end=' ')
        for j in range(i+1):
            print('@',end=' ')
        print()
    else:
        for _ in range(2*a-i-1):
            print('@',end=' ')
        print()