from collections import deque
N, K = map(int, input().split())

def bfs(N, K):
    dic = {}
    queue = deque()
    queue.append((N, 0))
    while True:
        x, y = queue.popleft()
        if x == K:
            cnt = y
            break
        if x<=-1 or x>=100001:
            continue
        if (2*x) not in dic:
            queue.append((2 * x, y + 1))
            dic[2*x] = True
        if (x+1) not in dic:
            queue.append((x+1, y+1))
            dic[x+1] = True
        if (x-1) not in dic:
            queue.append((x-1, y + 1))
            dic[x-1] = True
    return cnt

print(bfs(N, K))