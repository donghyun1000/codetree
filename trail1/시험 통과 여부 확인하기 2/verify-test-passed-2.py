t=int(input())
cnt=0
for tc in range(t):
    a=list(map(int,input().split()))
    sum=0
    for i in a:
        sum+=i
    avg=sum/len(a)
    if avg>=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
print(cnt)