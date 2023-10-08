import sys

input = sys.stdin.readline

n = int(input())
tower = list(int(input()) for _ in range(n))
stack = []
cnt = 0
for i in tower:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    cnt += len(stack) - 1

print(cnt)
