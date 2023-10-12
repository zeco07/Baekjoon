import sys

input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = list[0]
for i in range(1, n):
    for j in range(i):
        if list[j] < list[i]:
            dp[i] = max(dp[i], dp[j] + list[i])

        else:
            dp[i] = max(dp[i], list[i])

print(max(dp))
