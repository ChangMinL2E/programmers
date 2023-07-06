def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        move = numLog[i]-numLog[i-1]
        if move == -1:
            answer += 's'
        elif move == +1:
            answer += "w"
        elif move == -10:
            answer += "a"
        else:
            answer += "d"
    return answer