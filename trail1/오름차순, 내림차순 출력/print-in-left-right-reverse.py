a = int(input())
cnt=0
for i in range(a):
    for j in range(a):
        if i %2 ==0:
            cnt+=1
            print(cnt,end='')
            if cnt ==a:
                cnt=0
        else:
            print(a-cnt,end='')
            cnt+=1
            if cnt ==a:
                cnt=0
    print()