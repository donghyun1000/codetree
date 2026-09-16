a = int(input())

cnt=10
for i in range(a):
    for j in range(a):
        cnt-=1
        if cnt==0:
            cnt=9
        print(cnt,end='')
    print()