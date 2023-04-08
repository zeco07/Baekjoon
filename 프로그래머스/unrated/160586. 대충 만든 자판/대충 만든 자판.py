def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        sum = 0
        for j in targets[i]:
            chk = []
            print(j)
            for k in range(len(keymap)):
                if j in keymap[k]:
                    chk.append(keymap[k].index(j)+1)
            if chk:
                sum += min(chk)
            else:
                sum = -1
                break
        answer.append(sum)
    return answer
        