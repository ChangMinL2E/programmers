def solution(my_string, is_suffix):
    answer = 0
    lst = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in lst:
        answer = 1
    return answer