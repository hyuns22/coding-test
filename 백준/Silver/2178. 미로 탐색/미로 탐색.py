from collections import deque
def bfs(mp, N, M):
    x = 0
    y = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=N or ny <= -1 or ny>=M:
                continue
            if mp[nx][ny]==0:
                continue
            if mp[nx][ny]==1:

                queue.append((nx,ny))
                mp[nx][ny] = mp[x][y]+1
    return mp[N-1][M-1]




N, M = map(int, input().split())
mp = []
for i in range(N):
    a = list(map(int, input()))
    mp.append(a)

print(bfs(mp, N, M))