from itertools import permutations

def solution(k, dungeons):
    arr = list(permutations(dungeons,len(dungeons)))
    answer = []
    for i in range(len(arr)):
        tmp = k
        cnt = 0
        for j in range(len(arr[i])):
            if tmp >= arr[i][j][0]:
                tmp -= arr[i][j][1]
                cnt += 1
        answer.append(cnt)
    return max(answer)