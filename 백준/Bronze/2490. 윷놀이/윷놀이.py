li = []
for i in range(3):
    li.append([int(x) for x in input().split()])

for i in li:
    if sum(i) == 3:
        print('A')
    elif sum(i) == 2:
        print('B')
    elif sum(i) == 1:
        print('C')
    elif sum(i) == 0:
        print('D')
    else:
        print('E')