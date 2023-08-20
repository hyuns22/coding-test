import sys

N, M = map(int, sys.stdin.readline().split())


li = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    li.append(a)

sm = []
sm.append([li[0][0]])
for i in range(1, N):
    sm[0].append(li[0][i]+sm[0][i-1])
    sm.append([li[i][0]+sm[i-1][0]])

for i in range(1, N):
    for j in range(1, N):
        temp = li[i][j]+sm[i-1][j]+sm[i][j-1]-sm[i-1][j-1]
        sm[i].append(temp)

answer = []
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == 1 and y1 == 1:
        answer.append(sm[x2-1][y2-1])
        continue
    if x1 == 1:
        answer.append(sm[x2-1][y2-1] - sm[x2-1][y1-2])
        continue
    if y1 == 1:
        answer.append(sm[x2-1][y2-1] - sm[x1-2][y2-1])
        continue
    else:
        answer.append(sm[x2-1][y2-1]-sm[x2-1][y1-2]-sm[x1-2][y2-1]+sm[x1-2][y1-2])
        continue


for i in answer:
    print(i)