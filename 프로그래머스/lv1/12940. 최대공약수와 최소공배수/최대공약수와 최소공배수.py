def solution(n, m):
    answer = []
    if n>m:
        temp = m
        m = n
        n = temp
    for i in range(1, n+1):
        if n%i ==0 and m%i==0:
            num = i
    answer.append(num)
    answer.append(n*m//num) 
    return answer