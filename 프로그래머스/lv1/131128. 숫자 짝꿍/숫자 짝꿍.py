def solution(X, Y):
    lst_X = [0]*10
    lst_Y = [0]*10
    for x in X:
        lst_X[int(x)] += 1
    
    for y in Y:
        lst_Y[int(y)] += 1
        
    answer = ''
    
    for i in range(9,-1,-1):
        answer += (str(i)*min(lst_X[int(i)],lst_Y[int(i)]))
    
    if not len(answer):
        answer = "-1"
    elif answer.count("0") == len(answer):
        answer = "0"
    
    
    return answer