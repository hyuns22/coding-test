from collections import deque
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:

            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        k = queue.popleft()
        print(k, end=' ')

        for i in graph[k]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
graph = []
for i in range(N+1):
    graph.append([])
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
visited=[False]*(N+1)

dfs(graph, V, visited)

visited=[False]*(N+1)
print("")
bfs(graph, V, visited)