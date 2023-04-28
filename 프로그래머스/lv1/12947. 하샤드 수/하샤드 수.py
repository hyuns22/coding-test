def solution(x):
    list_x = str(x)
    list_int_x = list(map(int, list_x))
    if x%sum(list_int_x)==0:
        return True
    else:
        return False
    