def solution(strArr):
    answer = 0
    lst = list(map(lambda x: len(x), strArr))
    new_lst = list(set(lst))
    for i in new_lst:
        if answer < lst.count(i):
            answer = lst.count(i)
    return answer