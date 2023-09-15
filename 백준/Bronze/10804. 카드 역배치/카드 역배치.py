li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
li_tmp = []
for i in range(10):
    S1, S2 = map(int, input().split())
    for j in range(S1-1,S2):
        li_tmp.append(li[j])
    li_tmp.reverse()
    for k in range(len(li_tmp)):
        li[S1-1] = li_tmp.pop(0)
        S1 += 1

for i in li:
    print(i,end=' ')