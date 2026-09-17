a = int(input())
x=0
for i in range(a):
    for j in range(a):
        print(chr(ord('A') + x), end='')
        x+=1
    print()