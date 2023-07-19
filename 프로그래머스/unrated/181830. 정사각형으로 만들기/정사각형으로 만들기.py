def solution(arr):
    answer = arr[:]
    length = max(len(arr),len(arr[0]))
    if length > len(arr):
        for _ in range(length - len(arr)):
            answer.append([0]*(length))
    else:
        for i in range(len(arr)):
            lst = arr[i][:]
            for _ in range(len(arr)-len(arr[0])):
                lst.append(0)
            answer[i] = lst
        
        
    return answer