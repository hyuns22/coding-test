def star(N):
    if N == 3:
        return ['***', '* *', '***']
    else:
        L = []
        K = star(N//3)
        for i in range(N//3):
            L += [K[i]*3]
        for i in range(N//3):
            L += [K[i]+"   "*(N//9)+K[i]]
        for i in range(N//3):
            L += [K[i]*3]
        return L
N = int(input())


for k in star(N):
    print(k)