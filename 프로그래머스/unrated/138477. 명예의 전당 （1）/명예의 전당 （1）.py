def solution(k, score):
    answer = []
    li = []
    if len(score) > k:
        for i in range(k):
            li.append(score[i])
            li.sort(reverse=True)
            answer.append(li[-1])
        for i in range(k, len(score)):
            li.append(score[i])
            li.sort(reverse=True)
            answer.append(li[k-1])
    else:
        for i in range(len(score)):
            li.append(score[i])
            li.sort(reverse=True)
            answer.append(li[-1])
    return answer