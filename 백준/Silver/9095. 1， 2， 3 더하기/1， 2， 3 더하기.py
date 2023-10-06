import sys

input = sys.stdin.readline

t = int(input())


def ans(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return ans(n - 1) + ans(n - 2) + ans(n - 3)


for i in range(t):
    n = int(input())
    print(ans(n))
