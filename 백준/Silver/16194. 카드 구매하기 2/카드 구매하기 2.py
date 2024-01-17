N = int(input())
dp = [0]*(10000+1)
price = [0] + list(map(int, input().split()))

dp[1] = price[1]
mx = N*price[N]
for i in range(2, N+1):
    mn = mx
    for j in range(1, i+1):
        if dp[i-j]+price[j] < mn:
            mn = dp[i-j]+price[j]
    dp[i] = mn

print(dp[N])









