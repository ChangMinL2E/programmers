def solution(myString):
    answer = list(myString)
    
    for i in range(len(answer)):
        if ord(answer[i]) < ord('l'):
            answer[i] = 'l'
    answer = ''.join(answer)
    
    return answer