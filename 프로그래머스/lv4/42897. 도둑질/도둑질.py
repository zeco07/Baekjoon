def solution(money):
    n = len(money)
    dp1 = [0] * n # 첫 번째 집을 털었을 때의 최대 값
    dp2 = [0] * n # 첫 번째 집을 안 털었을 때의 최대 값

    # 첫 번째 집을 털었을 때
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])

    # 첫 번째 집을 안 털었을 때
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(dp1[-2], dp2[-1])
