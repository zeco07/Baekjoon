a = list(input())
b = list(input())

i = 0
while(i != len(a)):
    if b.count(a[i]) > 0:
        tmp = a[i]
        a.remove(tmp)
        b.remove(tmp)
    else:
        i+=1
print(len(a)+len(b))
