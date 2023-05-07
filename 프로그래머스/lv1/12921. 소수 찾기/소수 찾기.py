import math
def solution(n):
    answer = 0
    sosu = [True] *(n+1)
    a = math.ceil(n**0.5)
    for i in range(2, a+1):
        if sosu[i] == True:
            k=2
            while(i*k<=n):
                sosu[i*k]=False
                k+=1
    cnt = 0                
    for i in range(2, n+1):
        if sosu[i] == True:
            cnt+=1
    answer = cnt
    return answer