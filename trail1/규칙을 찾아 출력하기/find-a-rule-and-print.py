a = int(input())
for i in range(a): 
    if i==0 or i==(a-1):
        print('* '*a,end=' ')
    else:
        print('* '*i,end='')
        print(' '*(2*(a-i-1)),end='')
        print('*',end='')
    print()
