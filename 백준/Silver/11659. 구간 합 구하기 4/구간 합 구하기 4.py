import sys

input = sys.stdin.readline

n, m = map(int, input().split())

n_li = list(map(int, input().split()))
pfs = [0]
sum = 0
for i in n_li:
    sum += i
    pfs.append(sum)

for i in range(m):
    i, j = map(int, input().split())
    print(pfs[j] - pfs[i - 1])
