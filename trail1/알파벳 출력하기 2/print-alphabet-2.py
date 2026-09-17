a = int(input())
x=0
for i in range(a):
    print(' '*2*i,end='')
    for j in range(a-i):
        print(chr(ord('A')+x),end=' ')
        x+=1
        if x==26:
            x=0
    print()