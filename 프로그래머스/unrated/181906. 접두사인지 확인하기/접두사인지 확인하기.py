def solution(my_string, is_prefix):
    answer = 0
    lst = [my_string[:len(my_string)-i] for i in range(len(my_string))]
    if is_prefix in lst:
        answer = 1
    return answer