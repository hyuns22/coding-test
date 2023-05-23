n = int(input())

li = [[0]*3]
dp = [[0]*3 for i in range(n+1)]
for i in range(n):
    k = list(map(int, input().split()))
    li.append(k)
dp[1] = li[1]
for i in range(2,n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+li[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + li[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + li[i][2]

print(min(dp[n]))



