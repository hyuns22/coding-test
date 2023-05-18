from collections import deque
M, N, H = map(int, input().split())
box=[]
for i in range(H):
    box.append([])
    for j in range(N):
        a = list(map(int, input().split()))
        box[-1].append(a)
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i,j,k,0))

def bfs(box):

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while queue:
        x, y, z, v = queue.popleft()
        v+=1
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if nx <= -1 or ny <=-1 or nz<=-1 or nx>=H or ny>=N or nz>=M:
                continue
            if box[nx][ny][nz] == -1 or box[nx][ny][nz] == 1:
                continue
            if box[nx][ny][nz] == 0:
                box[nx][ny][nz] = 1
                queue.append((nx, ny, nz, v))
    return v-1
if len(queue)==0:
    print(-1)
else:
    ans = bfs(box)
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    ans = -1
    print(ans)





