import math

def solution(n):
    N = math.sqrt(n)
    if N-int(N) == 0:
        answer = (N+1)**2
    else:
        answer = -1
    return answer