import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(int(_) for _ in input().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 1:
                    map[nx][ny] = map[x][y] + 1
                    q.append((nx, ny))
    return map[n - 1][m - 1]


print(bfs(0, 0))
