def solution(k, m, score):
    answer = 0
    c = len(score)//m
    score.sort(reverse=True)
    sum = 0
    for i in range(c):
        li = score[m*i:m*(i+1)]
        sum += li[-1]*m
        
    return sum