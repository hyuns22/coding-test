from itertools import combinations
import math
def solution(nums):
    cnt = 0
    a = list(combinations(nums, 3))
    for i in range(len(a)):
        a[i] = sum(a[i])
    m = max(a)
    r_m = math.ceil(math.sqrt(m))
    num = set(range(2, m+1))
    for i in range(2, r_m+1):
        if i in num:
            num -= set(range(2*i, m+1, i))
    for i in a:
        if i in num:
            cnt +=1
    
    
    

    return cnt