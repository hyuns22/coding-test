
n = int(input())

dp = [i for i in range(n+1)]

m = int(n**0.5)

for i in range(2, m+1):
    for j in range(1, n+1):
        if j - i*i>=0:
            dp[j] = min(dp[j], dp[j-i*i]+1)

print(dp[n])


