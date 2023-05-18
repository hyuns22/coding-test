def binary_search(arr, start, end, find):
    mid = (start+end)//2
    if start > end:
        return '0'
    if arr[mid] == find:
        return '1'
    if arr[mid] > find:
        return binary_search(arr, start, mid-1, find)
    if arr[mid] < find:
        return binary_search(arr, mid+1, end, find)
N = int(input())
arr = list(map(int, input().split()))
M =int(input())
TEST = list(map(int, input().split()))

arr.sort()

for i in range(M):
    TEST[i] = binary_search(arr, 0, N-1, TEST[i])

s = " ".join(TEST)
print(s)



