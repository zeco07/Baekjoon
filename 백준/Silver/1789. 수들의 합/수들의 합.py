N = int(input())
sum = 0
for i in range(N+1):
    sum+=i+1
    if sum > N:
        print(i)
        break