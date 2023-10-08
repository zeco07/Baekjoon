import sys

input = sys.stdin.readline

n = int(input())

tower = list(map(int, input().split()))
stack = []
ans = []
for i in range(len(tower)):
    while stack:
        if stack[-1][0] < tower[i]:
            stack.pop()
        else:
            ans.append(stack[-1][1] + 1)
            break
    if not stack:
        ans.append(0)
    stack.append((tower[i], i))

print(*ans)
