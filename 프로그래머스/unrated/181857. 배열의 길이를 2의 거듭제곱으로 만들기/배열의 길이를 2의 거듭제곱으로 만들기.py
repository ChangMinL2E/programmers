def solution(arr):
    answer = arr[:]
    two_lst = []
    for i in range(0,11):
        two_lst.append(2**i)
    if not len(answer) in two_lst:
        for num in two_lst:
            if num > len(answer):
                new_lst = [0]*(num-len(answer))
                answer.extend(new_lst)
                break
    return answer