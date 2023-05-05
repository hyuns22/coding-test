import sys
sys.setrecursionlimit(10**6)
def dfs(graph, V, visited):
    visited[V] = True
    if graph[V] == []:
        return
    for i in graph[V]:
        if visited[i] == False:
            dfs(graph, i, visited)

N, M= map(int, sys.stdin.readline().split())
graph = []
for i in range(N+1):
    graph.append([])

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)
cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)