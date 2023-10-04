import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]


q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j, 0))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y, day = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    q.append((nx, ny, day + 1))

    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1

    return day


print(bfs())
