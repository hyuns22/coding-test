from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for i in goal:
        if len(cards1)!=0:
            if cards1[0] == i:
                cards1.popleft()
                continue
        if len(cards2)!=0:
            if cards2[0] == i and len(cards2)!=0:
                cards2.popleft()
                continue
        answer = 'No'
        break
        
    
   
    return answer