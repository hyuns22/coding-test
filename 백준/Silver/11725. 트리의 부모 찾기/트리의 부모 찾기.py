import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
MAP = []
DIC = {}

for i in range(N+1):
    MAP.append([])


for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    MAP[b].append(a)
    MAP[a].append(b)

visit = [False] * (N+1)
def dfs(MAP, n, visit):
    visit[n] = True
    if MAP[n] == []:
        return
    for i in MAP[n]:
        if visit[i] == False:
            DIC[i] = n
            dfs(MAP, i, visit)

dfs(MAP, 1, visit)

for i in range(2,N+1):
    print(DIC[i])


