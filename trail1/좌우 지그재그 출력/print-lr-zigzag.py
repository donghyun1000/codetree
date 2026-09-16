a = int(input())
cnt = 0
for i in range(a):
    for j in range(a):
        if i%2==0:
            cnt+=1
            print(cnt,end=' ')
        else:
            cnt+=1
            print(a*(i+1)-j, end=' ')
    print()