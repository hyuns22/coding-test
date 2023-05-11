def solution(N, stages):
    answer = []
    stage = []
    clear = []
    dic = {}
    for i in range(N):
        stage.append(0)
        clear.append(0)
    for i in stages:
        if i<=N:
            stage[i - 1] += 1
            for j in range(i):
                clear[j] += 1
        else:
            for j in range(N):
                clear[j] += 1
    
    for i in range(N):
        if clear[i] != 0:
            dic[i+1] = stage[i]/clear[i]
        else:
            dic[i+1] = 0
        
    dic = dict(sorted(dic.items(), key=lambda x : x[1], reverse=True))
    answer = list(dic.keys())
    return answer