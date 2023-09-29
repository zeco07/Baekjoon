import sys
input = sys.stdin.readline

n = int(input())
de_li = [int(i) for i in range(1,n+1)]
tmp_li = []
ans = ['+']
idx = 0
for i in range(n):
    num = int(input())
    while (len(tmp_li) != n):
        if idx == len(de_li):
            break
        if de_li[idx] == num:
            tmp_li.append(de_li.pop(idx))
            ans.append('-')
            if idx != 0:
                idx -= 1
            else:
                ans.append('+')
            break
        else:
            idx += 1
            ans.append('+')
ans.pop()
if len(tmp_li) == n:
    for i in ans:
        print(i)
else:
    print('NO')