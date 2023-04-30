def solution(s, n):
    answer = ''
    list_s = list(s)
    for i in range(len(list_s)):
        asc = ord(list_s[i])
        if 65<=asc<=90:
            asc += n
            if asc > 90:
                asc -= 26
        elif 97<=asc<=122:
            asc += n
            if asc >122:
                asc -= 26
        list_s[i] = chr(asc)
    answer = ''.join(list_s)
    return answer