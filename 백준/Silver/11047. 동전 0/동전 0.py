import sys

input = sys.stdin.readline

n, k = map(int, input().split())

a = [int(input()) for _ in range(n)]

cnt = 0
for i in reversed(range(n)):
    if k == 0:
        break
    cnt += k // a[i]
    k %= a[i]
print(cnt)