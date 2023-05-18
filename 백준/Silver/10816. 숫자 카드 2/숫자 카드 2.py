N = int(input())
arr = list(map(int, input().split()))
se_arr = list(set(arr))
di_arr = {}
se_arr.sort()
for i in arr:
    if i in di_arr:
        di_arr[i] += 1
    else:
        di_arr[i] = 1
M = int(input())
TEST = list(map(int, input().split()))

li = []
for i in range(M):
    cnt = 0
    start = 0
    end = len(se_arr)-1
    while start <= end:
        mid = (start+end) // 2
        if se_arr[mid] == TEST[i]:
            cnt = di_arr[se_arr[mid]]
            break
        if se_arr[mid] > TEST[i]:
            end = mid-1
            continue
        if se_arr[mid] < TEST[i]:
            start = mid+1
            continue
    li.append(str(cnt))
s = ' '.join(li)
print(s)

