a = int(input())
for i in range(1,a+1):
    for j in range(1,a+2-i):
        print(f'{i} * {j} = {i*j}', end=' ')
        if j ==a+1-i:
            print('',end='')
        else:
            print('/ ',end='')
    print()