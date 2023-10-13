import sys

input = sys.stdin.readline

n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + tp[i][0], n + 1):
        dp[j] = max(dp[i] + tp[i][1], dp[j])

print(dp[-1])
