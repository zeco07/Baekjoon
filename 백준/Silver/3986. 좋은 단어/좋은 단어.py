import sys
input = sys.stdin.readline

n = int(input())

count = 0
for i in range(n):
    string = input()
    stack = []
    for j in string:
        if stack == [] and j != '\n':
            stack.append(j)
        elif j == 'A':
            if stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(j)
        elif j == 'B':
            if stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(j)
    if stack:
        pass
    else:
        count += 1
print(count)