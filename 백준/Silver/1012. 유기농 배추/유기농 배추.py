import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

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
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for k in range(n):
        for l in range(m):
            if graph[k][l] == 1 and not visited[k][l]:
                visited[k][l] = True
                cnt += 1
                bfs(k, l)

    print(cnt)
