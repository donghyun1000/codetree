t = int(input())
for _ in range(t):
    a = int(input())
    cnt=0
    while a !=1:
        if a %2 ==0:
            a=a//2
            cnt+=1
        else:
            a=a*3+1
            cnt+=1
    print(cnt)