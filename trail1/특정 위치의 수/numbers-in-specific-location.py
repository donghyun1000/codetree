a = list(map(int,input().split()))
sum=0
for i in range(len(a)):
    if i==2 or i ==4 or i == 9:
        sum +=a[i]
print(sum)