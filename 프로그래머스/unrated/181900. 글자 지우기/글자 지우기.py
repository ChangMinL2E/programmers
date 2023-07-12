def solution(my_string, indices):
    answer = list(my_string)
    indices.sort(reverse=True)
    for idx in indices:
        answer.pop(idx)
    answer = ''.join(answer)
    return answer