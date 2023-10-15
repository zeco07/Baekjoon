import sys

input = sys.stdin.readline

n = int(input())
flowers = []
for i in range(n):
    flower = list(map(int, input().split()))
    flowers.append(
        [
            flower[0] * 100 + flower[1],
            flower[2] * 100 + flower[3],
        ]
    )

flowers.sort()
cnt = 0
end = 0
target = 301

while flowers:
    if target >= 1201 or target < flowers[0][0]:
        break

    for _ in range(len(flowers)):
        if target >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]
            flowers.remove(flowers[0])

        else:
            break

    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)
