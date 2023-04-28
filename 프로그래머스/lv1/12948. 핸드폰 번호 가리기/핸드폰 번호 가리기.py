def solution(phone_number):
    li = list(phone_number)
    for i in range(0, len(phone_number)-4):
        li[i]='*'
        
    return ''.join(li)