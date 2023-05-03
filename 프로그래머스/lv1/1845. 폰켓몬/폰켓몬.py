from itertools import combinations
def solution(nums):
    answer = 1
    n = len(set(nums))
    if n >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = n
    return answer