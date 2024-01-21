N, K = map(int, input().split())

dp = [[0]*(N+1) for i in range(K+1)]

for i in range(N+1):
    dp[1][i] = 1

for i in range(2, K+1):
    for j in range(0, N+1):
        dp[i][j] = sum(dp[i-1][:j+1])


print(dp[K][N]%1000000000)