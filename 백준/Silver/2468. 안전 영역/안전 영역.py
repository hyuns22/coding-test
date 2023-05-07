import copy
import sys
sys.setrecursionlimit(10**6)

def dfs(M, i, x, y):
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return
    if M[x][y] <= i:
        return
    M[x][y] = 0
    dfs(M, i, x+1, y)
    dfs(M, i, x - 1, y)
    dfs(M, i, x , y+1)
    dfs(M, i, x , y-1)


N = int(sys.stdin.readline())
MAP = []
mx = 0
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    if mx < max(a):
        mx = max(a)
    MAP.append(a)

li = []

for i in range(0, mx):
    cnt = 0
    temp_map = copy.deepcopy(MAP)
    for j in range(N):
        for k in range(N):
            if temp_map[j][k] > i:
                dfs(temp_map, i, j, k)
                cnt +=1
    li.append(cnt)

print(max(li))
