def solution(arr, queries):
    answer = arr[:]
    
    for lst in queries:
        st,ed = lst[0],lst[1]
        for i in range(st,ed+1):
            answer[i] += 1
    return answer