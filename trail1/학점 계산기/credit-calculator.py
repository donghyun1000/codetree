t = int(input())
n = list(map(float,input().split()))
avg = round(sum(n)/len(n),1)
if avg >= 4.0:
    print(avg)
    print('Perfect')
elif avg >= 3.0:
    print(avg)
    print('Good')
else:
    print(avg)
    print('Poor')