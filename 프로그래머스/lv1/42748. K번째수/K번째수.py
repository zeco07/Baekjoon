def solution(array, commands):
    answer =[]
    for start, end, idx in commands:
        arr = list(array[start-1:end])
        arr.sort()
        answer.append(arr[idx-1])
    return answer