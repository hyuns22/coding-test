from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    nx = [1, 0, -1, 0]
    ny = [0, 1, 0, -1]

    def bfs(maps, x, y):
        queue = deque()
        queue.append((x, y))
        while True:
            if len(queue) == 0:
                break
            x, y = queue.popleft()



            for i in range(4):
                dx = x + nx[i]
                dy = y + ny[i]
                if dx <= -1 or dx >= n or dy <= -1 or dy >= m:
                    continue
                if maps[dx][dy] == 0:
                    continue

                if maps[dx][dy] == 1:
                    maps[dx][dy] = maps[x][y] + 1
                    queue.append((dx, dy))

        return maps[n-1][m-1]
    if bfs(maps, 0, 0) == 1:
        answer = -1
        
    else:
        answer = bfs(maps, 0, 0)
    

    return answer