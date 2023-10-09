import sys
from collections import deque

input = sys.stdin.readline

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if building[nz][nx][ny] != "#" and not visited[nz][nx][ny]:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append((nz, nx, ny))

    if visited[ez][ex][ey] != 0:
        return f"Escaped in {visited[ez][ex][ey] - 1} minute(s)."
    else:
        return "Trapped!"


while True:
    l, r, c = map(int, input().split())
    if l + r + c == 0:
        break
    building = []
    for _ in range(l):
        floor = [list(input().strip()) for _ in range(r)]
        input()
        building.append(floor)

    visited = [list([0] * c for _ in range(r)) for _ in range(l)]

    q = deque()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == "S":
                    visited[i][j][k] = 1
                    q.append((i, j, k))
                elif building[i][j][k] == "E":
                    ez, ex, ey = i, j, k

    print(bfs())
