text = input()
l = list(text)
r = []
m = int(input())

for i in  range(m):
    command = input().split()
    if command[0] == 'L':
        if l:
            r.append(l.pop())
    elif command[0] == 'D':
        if r:
            l.append(r.pop())
    elif command[0] == 'B':
        if l:
            l.pop()
    elif command[0] == 'P':
        l.append(command[1])

print(''.join(l+r[::-1]))