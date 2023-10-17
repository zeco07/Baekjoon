import sys

input = sys.stdin.readline

n = int(input())
score = list(int(input()) for _ in range(n))
res = 0
cur = score[-1]
for i in reversed(range(n - 1)):
    cur = min(cur - 1, score[i])
    res += max(score[i] - cur, 0)

print(res)
