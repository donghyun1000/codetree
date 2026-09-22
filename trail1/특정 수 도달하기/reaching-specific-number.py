n = list(map(int,input().split()))
a=[]
for i in n:
    if i < 250:
        a.append(i)
        continue
    else:
        break
print(sum(a), round(sum(a)/len(a),1))