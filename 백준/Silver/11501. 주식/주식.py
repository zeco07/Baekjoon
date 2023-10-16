import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stock_price = list(map(int, input().split()))
    stock_price.reverse()
    maxv = 0
    profit = 0
    for i in range(n):
        if maxv < stock_price[i]:
            maxv = stock_price[i]
        else:
            profit += maxv - stock_price[i]

    print(profit)
