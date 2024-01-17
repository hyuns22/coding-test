N = int(input())
dp = [0]*(10000+1)
price = [0] + list(map(int, input().split()))

dp[1] = price[1]

for i in range(2, N+1):
    mx = 0
    for j in range(1, i+1):
        if dp[i-j]+price[j] > mx:
            mx = dp[i-j]+price[j]
    dp[i] = mx

print(dp[N])









