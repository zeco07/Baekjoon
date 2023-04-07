def solution(name, yearning, photo):
    answer = []
    for i in photo:
        sum = 0
        for j in i:
            if j in name:
                sum += yearning[name.index(j)]
        answer.append(sum)
    return answer