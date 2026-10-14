a = list(map(int, input().split()))
evens = a[1::2]
threes = a[2::3]
print(f'{sum(evens)} {sum(threes) / len(threes):.1f}')