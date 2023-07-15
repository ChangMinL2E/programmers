def solution(myString, pat):
    answer = ''
    for i in range(len(myString),len(pat)-1,-1):

        if myString[i-len(pat):i] == pat:
            answer = myString[:i]
            break
    return answer