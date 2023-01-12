N = int(input())

cnt = 0

while(N>=5):
    if(N%5 ==0):
        print(int(N/5)+cnt)
        break
    else:
        N -= 3
        cnt += 1
else:
    if(N%3==0):
        print(int(N/3)+cnt)
    else:
        print(-1)