t = int(input())
x=1
for tc in range(t):
    a, b = map(int,input().split())
    for i in range(a,b+1):
        x=x*i
    print(x)
    x=1