import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
list = [0] * (f + 1)


def bfs():
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        for nx in (x + u, x - d):
            if 0 < nx <= f and not list[nx] and nx != x:
                list[nx] = list[x] + 1
                q.append(nx)

    if list[g]:
        return list[g]
    else:
        return "use the stairs"


if g != s:
    print(bfs())
else:
    print(0)
