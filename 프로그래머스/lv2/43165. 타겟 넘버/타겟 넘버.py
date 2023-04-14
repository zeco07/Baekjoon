answer = 0

def dfs(num,tar,i,sum):
    global answer
    if i == len(num) and sum == tar:
        answer += 1
        return
    if i == len(num):
        return
    
    dfs(num,tar,i+1,sum+num[i])
    dfs(num,tar,i+1,sum-num[i])

def solution(numbers, target):
    global answer
    dfs(numbers,target,0,0)
    return answer