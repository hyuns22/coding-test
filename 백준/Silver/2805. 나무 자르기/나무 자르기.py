import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(tree)-1
a = 0
while True:
    mid = (start+end)//2
    result = 0
    for i in tree:
        if i > mid:
            result+= i-mid

    if result==M:
        a = mid
        break
    if start > end:
        a = end
        break

    if result > M:
        start = mid+1
    if result <M:
        end = mid-1
print(a)


