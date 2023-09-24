import sys
input = sys.stdin.readline
n = int(input())

stack = []

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])