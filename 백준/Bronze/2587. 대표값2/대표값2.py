li = []
for i in range(5):
    li.append(int(input()))
print(sum(li)//5)
li.sort()
print(li[2])