def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if yellow % i == 0 and (i + 2) * 2 + (yellow/i) * 2 == brown :
            if i >= yellow//i:
                answer.extend([i+2,yellow//i+2])
                break
            else:
                answer.extend([yellow//i+2,i+2])
                break
    return answer