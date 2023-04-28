def solution(players, callings):
    answer = []
    di = {}
    cnt = 0
    for i in players:
        di[i] = cnt
        cnt += 1

    for k in callings:
        ind = di[k]
        temp = players[ind-1]
        players[ind-1] = players[ind]
        players[ind] = temp
        di[players[ind-1]] -= 1
        di[players[ind]] += 1
        
        
    return players