N = int(input())
num = map(int, input().split())
result = 0
for i in num:
    cnt = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            result += 1
print(result)