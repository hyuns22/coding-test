import sys
sys.setrecursionlimit(10**6)

def dfs(li, x, y):
    global cnt
    if x<0 or y<0 or x>=N or y>=M:
        return False
    if li[x][y] == 'X':
        return False
    if li[x][y] == 'I':
        return False
    if li[x][y] == 'P':
        cnt += 1

    li[x][y] = 'I'


    dfs(li, x + 1, y)
    dfs(li, x -1, y)
    dfs(li, x , y+1)
    dfs(li, x , y-1)


N, M = map(int, input().split())

li = list()
for i in range(N):
    a = list(input())
    li.append(a)

cnt = 0
for i in range(N):
    for j in range(M):
        if li[i][j]=='I':
            dfs(li, i + 1, j)
            dfs(li, i - 1, j)
            dfs(li, i, j + 1)
            dfs(li, i, j - 1)

if cnt == 0:
    print("TT")
else:
    print(cnt)