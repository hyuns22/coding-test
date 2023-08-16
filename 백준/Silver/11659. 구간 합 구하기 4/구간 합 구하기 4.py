import sys
N, M = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    li[i] = li[i-1]+li[i]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    if s==1:
        print(li[e-1])
    else:
        print(li[e-1]-li[s-2])
