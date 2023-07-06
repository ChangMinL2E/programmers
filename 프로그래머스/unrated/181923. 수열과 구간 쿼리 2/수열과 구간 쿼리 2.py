def solution(arr, queries):
    answer = []
    for lst in queries:
        new_arr = arr[lst[0]:lst[1]+1]
        minimum = -1
        standard = lst[2]
        for i in new_arr:
            if i > standard:
                if minimum == -1:
                    minimum = i
                elif i < minimum:
                    minimum = i
        answer.append(minimum)
    return answer