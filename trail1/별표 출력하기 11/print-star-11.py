a = int(input())
for i in range(1,2*a+2):
    if i%2==1:
        print('* '*(2*a+1),end=' ')
    else:
        print('*   '*(a+1),end=' ')
    print()