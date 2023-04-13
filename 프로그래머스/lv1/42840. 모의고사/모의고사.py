def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    
    for i, j in enumerate(answers):
        if j == p1[i%len(p1)]:
            score[0] += 1
        if j == p2[i%len(p2)]:
            score[1] += 1
        if j == p3[i%len(p3)]:
            score[2] += 1
    for i, j in enumerate(score):
        if j == max(score):
            answer.append(i+1)
            
    return answer