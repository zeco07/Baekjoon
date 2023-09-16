N = [int(i) for i in input()]

set = [0] * 10

for i in N:
    if i == 6 or i == 9:
        if set[6] <= set[9]:
            set[6]+=1
        else:
            set[9]+=1
    else:
        set[i] += 1

print(max(set))