def solution(n):
    N = list(str(n))
    N = reversed(N)
    answer = []
    for i in N:
        answer.append(int(i))
    
    return answer