def solution(money):
    n = len(money)
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    #첫 번째 집 부터 터는 경우
    dp1[0] = money[0]
    dp1[1] = max(money[0],money[1])
    for i in range(2, n-1):         # 첫 번째 집을 털면 마지막 집은 못털어서 n-1 까지
        dp1[i] = max(dp1[i-1],dp1[i-2]+money[i])
    
    #두 번째 집 부터 터는 경우
    dp2[1] = money[1]
    for i in range(2,n):            # 마지막 집 털수 있어서 n 까지
        dp2[i] = max(dp2[i-1],dp2[i-2]+money[i])
    
    return max(max(dp1),max(dp2))