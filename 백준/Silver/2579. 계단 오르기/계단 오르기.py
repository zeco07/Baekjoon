import sys

input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

dp = [0] * n
if len(s) < 3:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[0] + s[2], s[1] + s[2])

    for i in range(3, n):
        dp[i] = max(s[i] + s[i - 1] + dp[i - 3], dp[i - 2] + s[i])

    print(dp[n - 1])
