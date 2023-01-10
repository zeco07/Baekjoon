T = int(input())

result = []
for i in range(T):
    H,W,N = map(int,input().split())

    people, floor = 0, 0
    num = 1
    while(people < N):
        people += 1
        if(floor == H):
            floor = 1
            num += 1
        else:
            floor += 1
    result.append(floor*100+num)

for i in result:
    print(i)