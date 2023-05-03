from collections import deque


def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        queue.append([progresses[i], speeds[i]])

    while True:
        if len(queue) == 0:
            break

        for i in range(len(queue)):
            queue[i][0] += queue[i][1]
        result = 0
        while True:
            if len(queue) == 0:
                break
            if queue[0][0] < 100:
                break
            result += 1
            queue.popleft()
        if result != 0:
            answer.append(result)

    return answer