def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i]//2 != 0:
            answer += str(i)*(food[i]//2)
    li = list(answer)
    r_li = list(reversed(li))
    answer = ''.join(li + ['0'] + r_li)
    return answer