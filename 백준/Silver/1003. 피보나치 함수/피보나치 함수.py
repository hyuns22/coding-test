n = int(input())
li=[]
for i in range(n):
    k = int(input())
    li.append(k)

dp = [[0, 0] for i in range(40+1)]

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0]+dp[i-2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for i in li:
    print(dp[i][0], dp[i][1])
