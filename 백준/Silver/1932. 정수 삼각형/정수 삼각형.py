import sys

input = sys.stdin.readline

n = int(input())
list = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(len(list[i])):
        if j == 0:
            list[i][j] += list[i - 1][j]
        elif j == len(list[i]) - 1:
            list[i][j] += list[i - 1][-1]
        else:
            list[i][j] += max(list[i - 1][j - 1], list[i - 1][j])

print(max(list[-1]))
