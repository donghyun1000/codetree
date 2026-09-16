a = int(input())
cnt=0
for i in range(a):
    for j in range(a):
        cnt +=2
        if cnt==10:
            cnt=2
        print(cnt,end=' ')
    print()