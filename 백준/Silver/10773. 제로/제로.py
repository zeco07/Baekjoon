import sys
input = sys.stdin.readline

k = int(input())
li = []
for i in range(k):
    num = int(input())
    if num == 0:
        li.pop()
    else:
        li.append(num)

print(sum(li))