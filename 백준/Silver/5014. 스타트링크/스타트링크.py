from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [0]*(F+1)
dl = [U, D*(-1)]

def bfs(visited):
    queue = deque()
    queue.append((S))
    visited[S] = 1

    while(queue):
        location = queue.popleft()

        for i in range(2):
            nl = location+dl[i]

            if nl > F or nl <=0:
                continue

            if visited[nl] == 0 or visited[nl] > visited[location]+1:
                visited[nl] = visited[location]+1
                queue.append(nl)
                continue



if S==G:
    print(0)
else:
    bfs(visited)
    if visited[G]==0:
        print("use the stairs")
    else:
        print(visited[G]-1)
