t = int(input())

result = []

for a in range(t):
    k = int(input())
    n = int(input())
    arr = [[0 for j in range(n)] for i in range(k+1)]
    for j in range(k+1):
        for i in range(n):
            if j == 0:
                arr[j][i] = i+1
            else:
                arr[j][i] = arr[j-1][i] + arr[j][i-1]
    result.append(arr[k][n-1])

for a in result:
    print(a)