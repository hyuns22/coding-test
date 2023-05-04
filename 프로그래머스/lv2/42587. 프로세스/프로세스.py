from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        if i == location:
            queue.append([priorities[i], True])
        else:
            queue.append([priorities[i], False])

    p = sorted(priorities, reverse=True)

    k = 0

    while True:
        if p[k] == queue[0][0] and queue[0][1] == True:
            k += 1
            break
        if queue[0][0] == p[k]:
            queue.popleft()
            k += 1
        else :
            queue.append(queue.popleft())


    answer = k
    return answer