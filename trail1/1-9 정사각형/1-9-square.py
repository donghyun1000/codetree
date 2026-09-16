a = int(input())
cnt=0
for i in range(a):
    for j in range(a):
        cnt+=1
        if cnt>=10:
            cnt-=9
        print(cnt,end='')
    print()