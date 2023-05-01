from itertools import combinations
def solution(numbers):
    arr = list(combinations(numbers, 2))
    for i in range(len(arr)):
        arr[i]=sum(arr[i])
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    answer = arr
    return answer