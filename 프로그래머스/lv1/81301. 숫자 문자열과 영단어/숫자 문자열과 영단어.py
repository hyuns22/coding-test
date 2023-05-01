def solution(s):
    s_li = list(s)
    answer = ''
    i = 0
    while(1):
        if i >= len(s_li):
            break
        if s_li[i] == 'z':
            answer += '0'
            i += 3
        elif s_li[i] == 'o':
            answer += '1'
            i += 2
        elif s_li[i] == 't' and s_li[i+1] == 'w':
            answer += '2'
            i += 2
        elif s_li[i] == 't' and s_li[i+1] == 'h':
            answer += '3'
            i += 4
        elif s_li[i] == 'f' and s_li[i+1] == 'o':
            answer += '4'
            i += 3
        elif s_li[i] == 'f' and s_li[i+1] == 'i':
            answer += '5'
            i += 3
        elif s_li[i] == 's' and s_li[i+1] == 'i':
            answer += '6'
            i += 2
        elif s_li[i] == 's' and s_li[i+1] == 'e':
            answer += '7'
            i += 4
        elif s_li[i] == 'e':
            answer += '8'
            i += 4
        elif s_li[i] == 'n':
            answer += '9'
            i += 3
        else:
            answer += str(s_li[i])
        i += 1
            
    print(answer)
    return int(answer)