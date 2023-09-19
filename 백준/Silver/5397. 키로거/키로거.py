Testcase = int(input())

keylog = []
l = [[] for _ in range(Testcase)]
r = [[] for _ in range(Testcase)]
for i in range(Testcase):
    keylog.append(input())
    for j in range(len(keylog[i])):
        # print(keylog[i][j])
        if keylog[i][j] == '<':
            if l[i]:
                r[i].append(l[i].pop())
        elif keylog[i][j] == '>':
            if r[i]:
                l[i].append(r[i].pop())
        elif keylog[i][j] == "-":
            if l[i]:
                l[i].pop()
        else:
            l[i].append(keylog[i][j])
for i in range(Testcase):
    password = "".join(l[i]) + "".join(r[i][::-1])  # l과 r 리스트를 합치고 r을 뒤집어서 비밀번호 생성
    print(password)