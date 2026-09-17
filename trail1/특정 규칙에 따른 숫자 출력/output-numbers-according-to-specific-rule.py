a = int(input())
cnt= 0
for i in range(a):
    for _ in range(i):
        print(' ', end=' ')
    for j in range(a-i,0,-1):
        cnt+=1
        if cnt == 10:
            cnt=1
        print(cnt,end=' ')
    print()