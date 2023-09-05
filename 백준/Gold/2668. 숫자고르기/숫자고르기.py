import sys
sys.setrecursionlimit(10**6)

N = int(input())
li = []
li.append(list(range(1, N+1)))
li.append([])
for i in range(N):
    a = int(input())
    li[1].append(a)


result = []
def dfs(n,visited, x):
    if visited[n] == True:
        return n
    visited[n] = True
    return dfs(li[1][n-1], visited, x)

visited = [False]*(N+1)
for i in range(1, N+1):
    if visited[i] == True:
        continue
    if dfs(i, visited, i) == i:
        result.append(i)
    visited = [False] * (N + 1)

print(len(result))
for i in result:
    print(i)

