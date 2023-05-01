def solution(strings, n):
    answer = []
    str_dict = {}
    for i in strings:
        if i[n] in str_dict:
            str_dict[i[n]] = str_dict[i[n]] + [i]
        else:
            str_dict[i[n]] = [i]
    str_dict = dict(sorted(str_dict.items()))
    for i in str_dict.values():
        i.sort()
        answer += i
    print(str_dict)
    return answer