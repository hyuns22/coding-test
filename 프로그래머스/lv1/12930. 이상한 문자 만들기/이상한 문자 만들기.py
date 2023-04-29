def solution(s):
    answer = ''
    arr = list(s)
    T_F = True
    
    for i in range(len(arr)):
        if arr[i] == ' ':
            T_F = True
        elif T_F == True:
            arr[i] = arr[i].upper()
            T_F = False
        elif T_F == False:
            arr[i] = arr[i].lower()
            T_F = True
    answer = ''.join(arr)
    return answer