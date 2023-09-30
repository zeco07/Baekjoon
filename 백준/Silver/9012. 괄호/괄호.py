import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    data = input()
    stack = []
    for j in data:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
    if stack:
        print('NO')
    else:
        print('YES')