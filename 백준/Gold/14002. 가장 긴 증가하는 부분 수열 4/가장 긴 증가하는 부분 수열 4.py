N = int(input())

A = [0] +list(map(int, input().split()))
dp = [0]* 1001

for i in range(1, N+1):
  mx = 0
  for j in range(0, i):
    if A[i]>A[j]:
      if mx<dp[j]:
        mx = dp[j]
  dp[i] = mx+1

tmp = max(dp)
print(tmp)
arr = []
for i in range(N, 0, -1):
  if tmp == dp[i]:
    tmp -= 1
    arr.append(A[i])

arr.reverse()

print(*arr)







