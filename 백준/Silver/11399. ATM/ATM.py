N = int(input())
arr = list(map(int, input().split()))
arr.sort()
su = 0
for i in range(N):
    su += sum(arr[0:i+1])

print(su)