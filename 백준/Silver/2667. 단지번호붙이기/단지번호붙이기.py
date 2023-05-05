def dfs(mp, x, y):
    global cnt
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return 0
    if mp[x][y] == 0:
        return 0

    if mp[x][y]==1:
        cnt += 1
        mp[x][y] = 0

        dfs(mp, x+1, y)
        dfs(mp, x-1, y)
        dfs(mp, x, y+1)
        dfs(mp, x , y-1)




N = int(input())
mp = []
li = []
for i in range(N):
    a = list(map(int, input()))
    mp.append(a)
num = 0
for i in range(N):
    for j in range(N):
        if mp[i][j] == 1:
            cnt = 0
            num+=1
            dfs(mp, i, j)
            li.append(cnt)
print(num)
li.sort()
for i in li:
    print(i)
