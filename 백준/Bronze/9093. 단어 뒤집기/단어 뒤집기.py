import sys

T = int(sys.stdin.readline())

for i in range(T):
    li = list(sys.stdin.readline().split())

    for j in li:
        tmp = list(reversed(list(j)))
        s = ''.join(tmp)
        print(s, end = ' ')




