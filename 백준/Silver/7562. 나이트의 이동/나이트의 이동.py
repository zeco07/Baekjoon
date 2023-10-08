import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [2, 1, 2, 1, -2, -1, -2, -1]
dy = [1, 2, -1, -2, 1, 2, -1, -2]


def bfs(cur_xy, goal_xy):
    q = deque()
    q.append(cur_xy)
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < i and 0 <= ny < i and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[goal_xy[0]][goal_xy[1]]


for _ in range(t):
    i = int(input())
    graph = [[0] * i for x in range(i)]
    visited = [[False] * i for x in range(i)]
    cur_xy = tuple(map(int, input().split()))
    goal_xy = tuple(map(int, input().split()))
    visited[cur_xy[0]][cur_xy[1]] = True
    print(bfs(cur_xy, goal_xy))
