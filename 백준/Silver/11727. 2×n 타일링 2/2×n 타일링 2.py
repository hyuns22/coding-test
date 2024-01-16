ipt = int(input())
dp = [0] * (1000+1)
dp[1] = 1
dp[2] = 3
for i in range(3, ipt+1):

    dp[i] = dp[i-1]+dp[i-2]*2

print(dp[ipt]%10007)
