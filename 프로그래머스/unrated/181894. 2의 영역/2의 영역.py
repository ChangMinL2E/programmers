def solution(arr):
    answer = []
    if arr.count(2) == 0:
        answer = [-1]
    elif arr.count(2) == 1:
        answer = [2]
    else:
        min_idx = 100001
        max_idx = -1
        for i in range(len(arr)):
            if arr[i] == 2:
                if i < min_idx:
                    min_idx = i
                if i > max_idx:
                    max_idx = i

        answer = arr[min_idx:max_idx+1]
    
    return answer