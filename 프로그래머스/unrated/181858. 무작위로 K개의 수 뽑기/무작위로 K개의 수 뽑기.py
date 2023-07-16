def solution(arr, k):
    answer = []
    
    for a in arr:
        if not a in answer and len(answer) != k:
            answer.append(a)
    if len(answer) < k:
        new_lst = [-1]*(k-len(answer))
        answer.extend(new_lst)
    return answer