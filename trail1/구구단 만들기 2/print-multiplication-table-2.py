a,b=map(int,input().split())

for i in range(4):
    for j in range(a,b+1):
        print(f'{a+b-j} * {2*i+2} = {(a+b-j)*(2*i+2)}',end=' ')
        if j < b:
            print('/',end=' ')
    print()