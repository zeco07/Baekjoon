import sys

input = sys.stdin.readline

n = int(input())
list = [list(map(int, input().split())) for _ in range(n)]
if n < 2:
    print(*list[0])
else:
    list[1][0] += list[0][0]
    list[1][1] += list[0][0]
    for i in range(2, n):
        for j in range(len(list[i])):
            if j == 0:
                list[i][j] += list[i - 1][j]
            elif j == len(list[i]) - 1:
                list[i][j] += list[i - 1][-1]
            else:
                list[i][j] += max(list[i - 1][j - 1], list[i - 1][j])

    print(max(list[-1]))
