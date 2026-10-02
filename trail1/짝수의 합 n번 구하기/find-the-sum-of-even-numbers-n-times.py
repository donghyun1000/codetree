n = int(input())
for tc in range(1,n+1):
    sum=0
    n,m=map(int,input().split())
    for i in range(n,m+1):
        if i%2==0:
            sum+=i
    print(sum)