import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()
time = [0] * n
time[0] = p[0]
for i in range(1, n):
    time[i] = p[i] + time[i - 1]
print(sum(time))
