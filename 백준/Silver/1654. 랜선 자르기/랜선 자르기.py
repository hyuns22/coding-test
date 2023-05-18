N, M = map(int, input().split())
LAN = []
for i in range(N):
    a = int(input())
    LAN.append(a)
start = 0
end = max(LAN)
a = 0
while True:
    mid = (start+end)//2
    if mid == 0:
        a = end
        break
    result = 0
    for i in LAN:
        result += i//mid

    if result==M and M%mid==0:
        a = mid
        break
    if start>end:
        a = end
        break
    if result >= M:
        start = mid+1
        continue
    if result <= M:
        end = mid-1
        continue
print(a)