from collections import deque
def bfs(pictures, x, y):
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1

    queue.append((x, y))
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<=-1 or ny<= -1 or nx>=n or ny>=m:
                continue
            if pictures[nx][ny] == 0:
                continue
            if pictures[nx][ny]==1:
                pictures[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt

n, m = map(int, input().split())
pictures = []
for i in range(n):
    a = list(map(int, input().split()))
    pictures.append(a)
li = []
for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1:
            pictures[i][j] = 0
            li.append(bfs(pictures, i, j))
if li == []:
    print(0)
    print(0)
else:
    print(len(li))
    print(max(li))

