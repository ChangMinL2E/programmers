def solution(n):
    answer = [n]
    
    while (answer[-1] != 1):
        a = answer[-1]
        if a%2:
            answer.append(a*3+1)
        else:
            answer.append(a/2)
    return answer