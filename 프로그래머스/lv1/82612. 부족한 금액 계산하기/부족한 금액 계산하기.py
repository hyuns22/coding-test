def solution(price, money, count):
    answer = money*(-1)
    answer += price*(count*(count+1)/2)
    if answer <= 0:
        answer = 0

    return answer