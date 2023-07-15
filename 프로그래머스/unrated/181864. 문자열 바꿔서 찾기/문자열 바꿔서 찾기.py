def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if myString[i] == 'A':
            myString = myString[:i]+'B'+myString[i+1:]
        elif myString[i] == 'B':
            myString = myString[:i]+'A'+myString[i+1:]

    if pat in myString:
        answer = 1
    
    return answer