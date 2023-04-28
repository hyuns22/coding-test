def solution(s):
    p_cnt = s.count('p')+s.count('P')
    y_cnt = s.count('y')+s.count('Y')
    
    
    if (p_cnt == y_cnt) or (p_cnt == 0 and y_cnt==0):
        return True
    else :
        return False

    