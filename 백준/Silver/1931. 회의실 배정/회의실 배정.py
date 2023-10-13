import sys

input = sys.stdin.readline

n = int(input())
schdule = [list(map(int, input().split())) for _ in range(n)]
schdule.sort(key=lambda x: (x[1],x[0]))
ans = [schdule[0]]

for i in range(1, n):
    if schdule[i][0] >= ans[-1][1]:
        ans.append(schdule[i])

print(len(ans))
