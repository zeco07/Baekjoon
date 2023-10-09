import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q_f:
        x, y = q_f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != "#" and not visited_f[nx][ny]:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_f.append((nx, ny))
    while q_s:
        x, y = q_s.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != "#" and not visited_s[nx][ny]:
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_s[x][y] + 1:
                        visited_s[nx][ny] = visited_s[x][y] + 1
                        q_s.append((nx, ny))
            else:
                return visited_s[x][y]

    return "IMPOSSIBLE"


for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(_ for _ in input().strip()) for _ in range(h)]
    visited_s = [[0] * w for _ in range(h)]
    visited_f = [[0] * w for _ in range(h)]
    q_s = deque()
    q_f = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@":
                visited_s[i][j] = 1
                q_s.append((i, j))
            elif graph[i][j] == "*":
                visited_f[i][j] = 1
                q_f.append((i, j))

    print(bfs())
