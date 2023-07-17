def solution(arr, delete_list):
    answer = arr[:]
    for ele in delete_list:
        if ele in answer:
            answer.remove(ele)
    return answer