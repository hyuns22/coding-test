answer = 0
def solution(numbers, target):
    
    def dfs(numbers, s, n, target):
        global answer
        if n == len(numbers):
            if s == target:
                answer+=1
            return
        dfs(numbers, s+numbers[n], n+1, target)
        dfs(numbers, s-numbers[n], n+1, target)
    dfs(numbers, 0, 0, target)
    return answer

