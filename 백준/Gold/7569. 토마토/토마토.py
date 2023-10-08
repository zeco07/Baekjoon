import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
box = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]


dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]


def bfs():
    while tomato:
        z, x, y, day = tomato.popleft()
        for j in range(6):
            nz = z + dz[j]
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = 1
                    tomato.append((nz, nx, ny, day + 1))

    for i in range(h):
        for j in range(n):
            if 0 in box[i][j]:
                return -1

    return day


tomato = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                tomato.append((i, j, k, 0))

print(bfs())
