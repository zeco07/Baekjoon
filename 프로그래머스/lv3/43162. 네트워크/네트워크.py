def dfs(x,computers,visited):
    visited[x] = True
    
    for a, b in enumerate(computers[x]):
        if b == 1 and not visited[a]:
            dfs(a,computers,visited)

def solution(n, computers):
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i,computers,visited)
            cnt += 1
    return cnt