from collections import deque
def bfs(BOX):
    queue = deque()

    for i in range(M):
        for j in range(N):
            if BOX[i][j] == 1:
                queue.append((i, j))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    day = 0
    while queue:

        for i in range(len(queue)):
            cnt = 0
            x, y = queue.popleft()
            for j in range(4):
                nx = x+dx[j]
                ny = y+dy[j]
                if nx<=-1 or nx>=M or ny<=-1 or ny>=N:
                    continue
                if BOX[nx][ny] == 1 or BOX[nx][ny] == -1:
                    continue
                if BOX[nx][ny] == 0:
                    queue.append((nx, ny))
                    BOX[nx][ny] = 1
                    cnt += 1
        day += 1
    state = True
    for i in range(M):
        for j in range(N):
            if BOX[i][j] == 0:
                state = False
                break
    if state == True:
        return day-1
    else:
        return -1


N, M = map(int, input().split())
BOX = []
for i in range(M):

        a = list(map(int, input().split()))
        BOX.append(a)



print(bfs(BOX))

