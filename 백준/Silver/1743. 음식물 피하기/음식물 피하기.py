import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    global cnt
    if x<=-1 or y<= -1 or x>=N or y>=M:
        return False
    if graph[x][y] == 1:
        graph[x][y]=0
        cnt+=1
        dfs(x-1, y)
        dfs(x +1, y)
        dfs(x , y+1)
        dfs(x , y-1)
    return False



N, M, K = map(int, input().split())

graph = []
for i in range(N):
    a = []
    for j in range(M):
        a.append(0)
    graph.append(a)

for i in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1



t_cnt = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            if t_cnt < cnt:
                t_cnt = cnt

print(t_cnt)