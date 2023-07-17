def solution(n_str):
    answer = n_str[:]
    while True:
        if answer[0] == '0':
            answer = answer[1:]
        else:
            break
    return answer