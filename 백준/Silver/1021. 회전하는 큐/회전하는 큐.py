import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,(input().split()))
order = list(map(int,(input().split())))
q = deque([int(i) for i in range(1,n+1)])

count = 0

for i in order:
    while True:
        avg = len(q)//2
        if i == q[0] :
            q.popleft()
            break
        elif q.index(i) > avg :
            q.rotate(1)
            count += 1
        else :
            q.rotate(-1)
            count += 1
print(count)