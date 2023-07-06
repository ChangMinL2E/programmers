def solution(arr, queries):
    answer = arr[:]
    for lst in queries:
        a,b = lst[0],lst[1]
        answer[a], answer[b] = answer[b], answer[a]
    
    
    return answer