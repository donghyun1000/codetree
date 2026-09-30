a = list(map(int,input().split()))
cnt=0
sum_a=0
for i in range(len(a)):
    if a[i] ==0:
        break
    if a[i]%2==0:
        cnt+=1
        sum_a+=a[i]
print(cnt, sum_a)