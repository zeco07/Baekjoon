import sys
from collections import deque

input = sys.stdin.readline
ans = deque()
for i in range(int(input())):
    command = list(input().split())
    if command[0] == 'push_front':
        ans.appendleft(command[1])
    elif command[0] == 'push_back':
        ans.append(command[1])
    elif command[0] == 'pop_front':
        if len(ans) > 0 :print(ans.popleft())
        else : print(-1)
    elif command[0] == 'pop_back':
        if len(ans) > 0 : print(ans.pop())
        else : print(-1)
    elif command[0] == 'size':
        print(len(ans))
    elif command[0] == 'empty':
        if len(ans) == 0 : print(1)
        else : print(0)
    elif command[0] == 'front':
        if len(ans) > 0 : print(ans[0])
        else : print(-1)
    elif command[0] == 'back':
        if len(ans) > 0 : print(ans[len(ans)-1])
        else : print(-1)