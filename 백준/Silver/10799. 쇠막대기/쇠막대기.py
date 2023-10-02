map = input()

stack = []
ans = 0
for i in range(len(map)):
    if map[i] == '(':
        stack.append(map[i])
    else:
        if map[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            ans += len(stack.pop())
print(ans)