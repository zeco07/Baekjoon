N, K = map(int, input().split())
li = [[0,0,0,0,0,0], [0,0,0,0,0,0]]
for i in range(N):
    S, Y = map(int, input().split())
    li[S][Y-1]+=1
count = 0
for i in range(len(li)):
    for j in li[i]:
        if j != 0 and j <= K:
            count += 1
        elif j != 0 and j > K:
            if j%K == 0:
                count += j//K
            else:
                count += j//K+1
print(count)
