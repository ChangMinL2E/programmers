def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            new_lst = [arr[i]]*arr[i]*2
            answer.extend(new_lst)
        else:
            for _ in range(arr[i]):
                answer.pop()
            
    return answer