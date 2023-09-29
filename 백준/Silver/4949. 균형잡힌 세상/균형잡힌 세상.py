import sys
input = sys.stdin.readline
ans = []
while True:
    string = input()
    if string == '.\n':
        break
    check = []
    for a in string:
        for b in a:
            if '(' == b or ')'==b or '['==b or ']'==b:
                check.append(b)
    check = ''.join(check)
    while True:
        if len(check) == 0:
            ans.append('yes')
            break
        if '()' in check:
            check = check.replace('()','')
            continue
        elif '[]' in check:
            check = check.replace('[]','')
            continue
        else:
            ans.append('no')
            break
    
for i in ans:
    print(i)