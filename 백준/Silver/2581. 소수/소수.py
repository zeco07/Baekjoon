M = int(input())
N = int(input())

result = 0

if (M <= N and M+N <= 20000):
    for i in range(M,N+1):
        cnt = 0
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    cnt += 1
            if cnt == 0:
                if result == 0:
                    min = i
                result += i
if result != 0:
    print(result)
    print(min)
else:
    print(-1)