a = int(input())

for i in range(a):
    for j in range(a-i):
        print('*'*(a-i),end='')
        if j < (a-i)-1:      # 마지막 덩어리가 아니면
            print(' ', end='')
    print()