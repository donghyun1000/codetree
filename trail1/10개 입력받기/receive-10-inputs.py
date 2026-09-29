a = list(map(int,input().split()))
sum=0
cnt=0
for i in a:
    if i ==0:
        break
    sum +=i
    cnt+=1
print(sum, round(sum/cnt,1))
