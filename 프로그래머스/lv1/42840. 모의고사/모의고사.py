def solution(answers):
    answer = []
    cnt_1=0
    cnt_2=0
    cnt_3=0
    for i in range(len(answers)):
        if i % 5 == 0:
            if answers[i] == 1:
                cnt_1+=1
        elif i % 5 == 1:
            if answers[i] == 2:
                cnt_1+=1
        elif i % 5 == 2:
            if answers[i] == 3:
                cnt_1+=1
        elif i % 5 == 3:
            if answers[i] == 4:
                cnt_1+=1
        elif i % 5 == 4:
            if answers[i] == 5:
                cnt_1+=1
                
        if i%2 == 0:
            if answers[i] == 2:
                cnt_2+=1
        elif i//2%4 == 0:
            if answers[i] == 1:
                cnt_2+=1
        elif i//2%4 == 1:
            if answers[i] == 3:
                cnt_2+=1
        elif i//2%4 == 2:
            if answers[i] == 4:
                cnt_2+=1
        elif i//2%4 == 3:
            if answers[i] == 5:
                cnt_2+=1
        
        if i//2%5 == 0:
            if answers[i] == 3:
                cnt_3+=1
        elif i//2%5 == 1:
            if answers[i] == 1:
                cnt_3+=1
        elif i//2%5 == 2:
            if answers[i] == 2:
                cnt_3+=1
        elif i//2%5 == 3:
            if answers[i] == 4:
                cnt_3+=1
        elif i//2%5 == 4:
            if answers[i] == 5:
                cnt_3+=1
    answer=[cnt_1, cnt_2, cnt_3]
    m = max(answer)
    li = []
    for i in range(3):
        if answer[i] == m:
            li.append(i+1)
    
    return li