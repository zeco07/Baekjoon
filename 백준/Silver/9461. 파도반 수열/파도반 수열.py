import sys

input = sys.stdin.readline

t = int(input())
p = [0] * 101
p[0] = p[1] = p[2] = 1
for _ in range(t):
    n = int(input())
    if n < 3:
        print(1)
    else:
        for i in range(3, n):
            p[i] = p[i - 2] + p[i - 3]
        print(p[n - 1])
