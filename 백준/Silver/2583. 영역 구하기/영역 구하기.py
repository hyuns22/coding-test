from collections import deque
import sys
M, N, K = map(int, sys.stdin.readline().split())

MAP = []
li = []
for i in range(M):
    MAP.append([])
    for j in range(N):
        MAP[-1].append(0)

for i in range(K):
    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
    for j in range(y_2-y_1):
        for k in range(x_2-x_1):
            MAP[y_1+j][x_1+k] = 1

queue = deque()
cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(M):
    for j in range(N):
        if MAP[i][j] == 0:
            cnt+=1
            queue.append((j, i))
            temp_cnt = 0
            while queue:
                x, y = queue.popleft()


                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]

                    if nx <= -1 or nx >= N or ny<= -1 or ny>=M:
                        continue
                    if MAP[ny][nx] == 1:
                        continue
                    MAP[ny][nx] = 1
                    temp_cnt += 1
                    queue.append((nx, ny))
            if temp_cnt == 0:
                temp_cnt+=1
            li.append(temp_cnt)
li.sort()


print(cnt)
for i in li:
    print(i, end=" ")



