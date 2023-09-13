def b_s(note1, start, end, ans):
    while(True):
        mid = (start+end)//2
        if start > end:
            return 0

        if note1[mid] == ans:
            return 1
        elif note1[mid] < ans:
            start = mid+1
        else:
            end = mid-1


T = int(input())
for t in range(T):

    N = int(input())
    note1 = []

    note1 = list(map(int, input().split()))


    M = int(input())
    note2 = []

    note2 = list(map(int, input().split()))

    note1.sort()

    result = []
    for i in range(M):
        result.append(b_s(note1, 0, N-1, note2[i]))

    for i in result:
        print(i)