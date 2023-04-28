def solution(n):
    str_list = list(str(n))
    str_list.sort(reverse=True)
    str_n = ''.join(str_list)
    answer = int(str_n)
    return answer