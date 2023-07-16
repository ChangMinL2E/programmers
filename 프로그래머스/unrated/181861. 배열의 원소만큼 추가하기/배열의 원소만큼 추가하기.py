def solution(arr):
    answer = []
    
    for num in arr:
        new_lst = [num]*num
        answer.extend(new_lst)
    return answer