li1 = []
for i in range(9):
    li1.append(int(input()))

for i in range(len(li1)-1):
    for j in range(i+1,len(li1)):
        if sum(li1)-(li1[i]+li1[j]) == 100:
            li1.remove(li1[i])
            li1.remove(li1[j-1])
            break

li1.sort()

for i in li1:
    print(i)