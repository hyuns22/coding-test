def dfs(li, p, s, c, visit):
    global cnt
    if visit[p] == True:
        return
    if s in li[p]:
        cnt = c
        return 
    visit[p] = True
        
    for i in li[p]:
        dfs(li, i, s, c+1, visit)


N = int(input())
A, B = map(int, input().split())
M = int(input())
li = []

for i in range(N+1):
    li.append([])

for i in range(M):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

visit = [False]*(N+1)
cnt = 0
dfs(li, A, B, 1, visit)
if cnt == 0:
    cnt = -1
print(cnt)