import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
ans = 0
for i in a:
    ans += i * max(b)
    b.pop(b.index(max(b)))

print(ans)