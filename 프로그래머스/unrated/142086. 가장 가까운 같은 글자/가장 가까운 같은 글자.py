def solution(s):
    answer = []
    dic = {}
    s_li = list(s)
    for i in range(len(s_li)):
        if s_li[i] in dic:
            answer.append(i-dic[s_li[i]])
            dic[s_li[i]] = i
        else:
            dic[s_li[i]] = i
            answer.append(-1)
    return answer