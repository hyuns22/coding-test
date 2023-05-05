import sys
sys.setrecursionlimit(10**6)
def dfs(MAP, color, x, y):
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return
    if MAP[x][y] != color:
        return
    MAP[x][y] = 0
    dfs(MAP, color, x+1, y)
    dfs(MAP, color, x-1, y)
    dfs(MAP, color, x, y+1)
    dfs(MAP, color, x, y-1)
N = int(sys.stdin.readline())
MAP = []
MAP_1 = []
for i in range(N):
    a = sys.stdin.readline()
    MAP.append(list(a))
    a = a.replace('G', 'R')
    MAP_1.append(list(a))
cnt = 0
cnt_1 = 0
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 'R':
            dfs(MAP, 'R', i, j)
            cnt+=1
        elif MAP[i][j] == 'G':
            dfs(MAP, 'G', i, j)
            cnt+=1
        elif MAP[i][j] == 'B':
            dfs(MAP, 'B', i, j)
            cnt+=1
        if MAP_1[i][j] == 'R':
            dfs(MAP_1, 'R', i, j)
            cnt_1+=1
        elif MAP_1[i][j] == 'B':
            dfs(MAP_1, 'B', i, j)
            cnt_1+=1
print(cnt, cnt_1)