from collections import deque
def bfs(graph, infection):
    cnt = 0
    queue = deque()
    queue.append(1)
    infection[1] = True
    while queue:
        k = queue.popleft()
        for i in graph[k]:
            if infection[i] == False:
                infection[i] = True
                cnt+=1
                queue.append(i)
    return cnt



N = int(input())
M = int(input())
graph = [[]]
for i in range(N):
    graph.append([])

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

infection = [False]*(N+1)

print(bfs(graph, infection))