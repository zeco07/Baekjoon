import sys

input = sys.stdin.readline

n = int(input())
positive = []
negative = []
res = 0
for i in range(n):
    a = int(input())
    if a == 1:
        res += 1
    elif a > 0:
        positive.append(a)
    else:
        negative.append(a)

positive.sort()
negative.sort(reverse=True)

while positive:
    if len(positive) == 1:
        res += positive.pop()
    else:
        res += positive.pop() * positive.pop()

while negative:
    if len(negative) == 1:
        res += negative.pop()
    else:
        res += negative.pop() * negative.pop()

print(res)
