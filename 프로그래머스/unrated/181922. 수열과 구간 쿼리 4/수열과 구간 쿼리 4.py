def solution(arr, queries):
    answer = arr[:]
    for q in queries:
        for i in range(q[0],q[1]+1):
            if not(i % q[2]):
                answer[i] += 1
    
    return answer