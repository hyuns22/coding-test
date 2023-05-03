from collections import deque
def solution(s):
    answer = True
    queue = deque()
    s_li = list(s)
    for i in s_li:
        if i == '(':
            queue.append(i)
        if i == ')':
            if len(queue) == 0:
                return False
            else:
                queue.popleft()
    
    if len(queue) == 0:
        return True
    else:
        return False