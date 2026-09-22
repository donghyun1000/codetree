n = list(map(int,input().split()))
a=[]
for i in n:
    if i ==0:
        break
    else:
        a.append(i)
print(*a[-1::-1])