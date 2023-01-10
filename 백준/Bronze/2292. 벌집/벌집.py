N = int(input())

a = 1
b = 6
c = a+b
while(N>1):
    if (c >= N):
        print(a+1)
        break
    a += 1
    c += b*a 
else:
    print(1)