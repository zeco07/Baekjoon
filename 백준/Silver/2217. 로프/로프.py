import sys

input = sys.stdin.readline

n = int(input())
rope = list(int(input()) for _ in range(n))
rope.sort()
ans = []

for i in range(n):
    ans.append(rope[i] * (n - i))

print(max(ans))
