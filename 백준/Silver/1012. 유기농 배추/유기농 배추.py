import sys
sys.setrecursionlimit(5000)

def dfs(MAP, x, y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return
    if MAP[x][y] == 0:
        return
    if MAP[x][y] == 1:
        MAP[x][y] = 0
        dfs(MAP, x+1, y)
        dfs(MAP, x-1, y)
        dfs(MAP, x, y+1)
        dfs(MAP, x, y-1)

li = []
T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    MAP = []
    for i in range(N):
        MAP.append([])
        for j in range(M):
            MAP[i].append(0)
    for i in range(K):
        a, b = map(int, input().split())
        MAP[a][b] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                cnt +=1
                dfs(MAP, i, j)

    li.append(cnt)

for i in li:
    print(i)

