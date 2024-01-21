n = int(input())

li = [-1001] + list(map(int, input().split()))
dp = [-1001] * (n+1)
dp[1] = li[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1]+li[i], li[i])

print(max(dp))






