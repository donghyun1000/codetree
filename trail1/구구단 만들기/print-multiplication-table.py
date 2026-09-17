a,b=map(int,input().split())
for i in range(1,10):
    for j in range(a,b+1):
        if (j)%2==0:
            print(f'{a+b-j} * {i} = {(a+b-j)*i}',end='')
            if j<b-1:
                print(' /', end=' ')
    print()