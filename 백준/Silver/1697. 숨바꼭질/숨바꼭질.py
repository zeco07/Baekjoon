import sys
from collections import deque

MAX = 100001

input = sys.stdin.readline

n, k = map(int, input().split())
list = [0] * MAX


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(list[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not list[nx]:
                list[nx] = list[x] + 1
                q.append(nx)


bfs()
