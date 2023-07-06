def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = (mode + 1)%2
        else:
            if mode == 0 and not i%2:
                answer += code[i]
            elif mode == 1 and i%2:
                answer += code[i]
    if not len(answer):
        answer = "EMPTY"
    
    return answer

