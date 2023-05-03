import datetime

def solution(a, b):
    li = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = ''
    day1 = datetime.datetime(2016, 1, 1)
    day2 = datetime.datetime(2016, a, b)
    answer = li[(day2-day1).days%7]
    return answer