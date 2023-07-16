def solution(arr, n):
    answer = arr[:]
    for i in range(len(answer)):
        if (len(answer)+i)%2:
            answer[i] += n
    return answer