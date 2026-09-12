a = int(input())
for i in range(a):
    print(' '.join('*'*(a-i)))
for i in range(2,a+1):
    print(' '.join('*'*i))