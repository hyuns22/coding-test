N, M = map(int, input().split())

li = list(map(int, input().split()))

start = max(li)
end = sum(li)

while (start<=end):
    mid = (start+end)//2

    cnt = 0
    t_sum = 0

    for i in li:
        t_sum += i
        if t_sum > mid:
            t_sum = 0
            t_sum+=i
            cnt += 1
        elif t_sum==mid:
            t_sum = 0
            cnt +=1

    if t_sum != 0:
        cnt += 1




    if cnt <= M:
        end = mid-1
    else:
        start = mid+1


print(start)