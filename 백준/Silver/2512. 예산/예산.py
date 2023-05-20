N = int(input())
li = list(map(int, input().split()))
M = int(input())
li.sort()
start = 0
end = li[-1]
ans = 0
while True:
    mid = (start+end)//2
    result = 0
    for i in li:
        if mid > i:
            result+=i
        else:
            result+=mid
    if start>end:
        ans = end
        break
    if result == M:
        ans = mid
        break
    if result < M:
        start = mid+1
    elif result > M:
        end = mid -1
print(ans)





