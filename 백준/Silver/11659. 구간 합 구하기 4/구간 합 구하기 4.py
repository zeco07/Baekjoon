import sys

input = sys.stdin.readline

n, m = map(int, input().split())

n_li = list(map(int, input().split()))

dp = [0] * n
dp[0] = n_li[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + n_li[i]

for _ in range(m):
    i, j = map(int, input().split())
    if i < 2:
        print(dp[j - 1])
    else:
        print(dp[j - 1] - dp[i - 2])
