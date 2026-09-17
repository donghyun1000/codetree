a = int(input())
for i in range(1,a+1):
    for j in range(i,0,-1):
        print(a-j+1,end=' ')
    print()