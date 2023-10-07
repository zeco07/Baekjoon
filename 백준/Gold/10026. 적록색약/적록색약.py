import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(_ for _ in input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            bfs(i, j)

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

visited = [[False] * n for _ in range(n)]

cnt_1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            cnt_1 += 1
            bfs(i, j)

print(cnt, cnt_1)
