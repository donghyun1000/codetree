a = int(input())

for i in range(a):
    for j in range(a):
        print(f'({a-i},{a-j})',end=' ')
    print()