def solution(target):
    answer = [0, 0]
    single_or_bull = [i for i in range(1, 21)] + [50]
    double_or_triple = list(set([i*2 for i in range(1, 21) if i * 2 > 20] + [i*3 for i in range(1, 21) if i * 3 > 20]))

    dp = [[100001, 0] for _ in range(target+1)]
    dp[0] = [0, 0]
    for i in filter(lambda x: x <= target, single_or_bull):
        dp[i] = [1, 1]
        
    for i in filter(lambda x: x <= target, double_or_triple):
        dp[i] = [1, 0]
        
    for s in single_or_bull + double_or_triple:
        for i in range(s, target + 1):
            if dp[i][0] > (sum_of_dp := dp[i - s][0] + dp[s][0]):
                dp[i] = [sum(x) for x in zip(dp[i - s], dp[s])]
            elif sum_of_dp == dp[i][0] and dp[i][1] < dp[i - s][1] + dp[s][1]:
                dp[i] = [sum(x) for x in zip(dp[i - s], dp[s])]
        
    return dp[target]