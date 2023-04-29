def solution(n):
    arr = []
    while(n//3!=0):
        arr.append(n%3)
        n = n//3
    arr.append(n)
    arr.reverse()
    sum=0
    for i in range(len(arr)):
        sum += arr[i]*(3**i)
    answer = sum
    return answer
