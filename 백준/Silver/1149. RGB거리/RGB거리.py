dp = [[0, 0, 0] for i in range(1001)]

T = int(input())

cost = [0]

for i in range(T):
    a = list(map(int, input().split()))
    cost.append(a)

dp[1] = cost[1]
for i in range(2, T+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])+cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])+cost[i][2]


print(min(dp[T]))


