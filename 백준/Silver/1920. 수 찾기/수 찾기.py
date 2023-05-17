import sys
sys.setrecursionlimit(10**6)

def binary_search(arr, find, start, end):
    mid = (start+end) // 2
    if arr[mid] == find:
        return 1
    if start >= end:
        return 0
    if arr[mid] < find:
        return binary_search(arr, find, mid+1, end)
    elif arr[mid] > find:
        return binary_search(arr, find, start, mid-1)



N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
arr1 = list(map(int, input().split()))

for i in range(len(arr1)):
    arr1[i] = binary_search(arr, arr1[i], 0, N-1)

for i in arr1:
    print(i)