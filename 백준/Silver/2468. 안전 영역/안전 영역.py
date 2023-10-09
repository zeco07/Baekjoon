import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_h = 0
for i in range(n):
    for j in range(n):
        max_h = max(max_h, graph[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


max_area = 0
for i in range(1, max_h):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[j][k]:
                visited[j][k] = True
                cnt += 1
                bfs(j, k, i)
    max_area = max(max_area, cnt)

if max_h == 1:
    print(1)
else:
    print(max_area)
