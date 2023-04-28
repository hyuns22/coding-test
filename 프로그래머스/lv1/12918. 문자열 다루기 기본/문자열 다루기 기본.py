def solution(s):
    answer = True
    if 4 == len(s) or len(s)== 6:
        try:
            s = int(s)
            
        except:
            answer = False
    else:
        answer = False
    return answer