N = int(input())

li = list(map(int, input().split()))
Y = M = 0
for i in li:
    Y += (i//30 + 1)*10
    M += (i//60 + 1)*15
    
if Y > M:
    print(f'M {M}')
elif M > Y:
    print(f'Y {Y}')
else:
    print(f'Y M {Y}')