def solution(str_list, ex):
    answer = list(filter(lambda x: not ex in x, str_list))
    answer = ''.join(answer)
    return answer