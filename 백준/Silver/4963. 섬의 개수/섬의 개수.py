import sys
sys.setrecursionlimit(10**6)
def dfs(MAP, x, y):
    if x<=-1 or x>=h or y<=-1 or y>=w:
        return
    if MAP[x][y]==0:
        return
    MAP[x][y] = 0
    dfs(MAP, x+1, y)
    dfs(MAP, x-1, y)
    dfs(MAP, x, y+1)
    dfs(MAP, x, y-1)
    dfs(MAP, x+1, y+1)
    dfs(MAP, x -1, y - 1)
    dfs(MAP, x - 1, y + 1)
    dfs(MAP, x + 1, y - 1)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w ==0 and h==0:
        break
    MAP = []
    for i in range(h):
        a = list(map(int, sys.stdin.readline().split()))
        MAP.append(a)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                dfs(MAP, i, j)
                cnt += 1
    print(cnt)