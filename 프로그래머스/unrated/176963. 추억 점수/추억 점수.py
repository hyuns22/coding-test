def solution(name, yearning, photo):
    name_score={}
    answer = []
    for i in range(len(name)):
        name_score[name[i]] = yearning[i]
    
    for i in photo:
        sum = 0
        
        for k in i:
            if k in name:
                sum = sum + name_score[k]
        answer.append(sum)
        
    return answer