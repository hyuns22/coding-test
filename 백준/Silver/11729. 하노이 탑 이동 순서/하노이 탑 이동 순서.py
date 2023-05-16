def hanoi(N, p, q, r):
    if N == 1:
        return [p, q]
    else:
        return hanoi(N-1, p, r, q) + [p, q] + hanoi(N-1, r, q, p)

N = int(input())

L = hanoi(N, 1, 3, 2)

cnt = len(L)//2
print(cnt)
for i in range(cnt):
    print(L[2*i], L[2*i+1])

