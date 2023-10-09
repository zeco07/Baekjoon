import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for _ in range(k):
    s_y, s_x, e_y, e_x = map(int, input().split())
    for i in range(s_x, e_x):
        for j in range(s_y, e_y):
            graph[i][j] += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    area = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    area += 1
                    q.append((nx, ny))
    return area


ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print(*ans)
