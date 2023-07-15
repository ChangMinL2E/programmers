def solution(myString):
    answer = sorted(myString.split('x'))
    for i in range(len(answer)-1,-1,-1):
        if len(answer[i]) == 0:
            answer.pop(i)
    return answer