def solution(arr):
    answer = []
    i = 0
    stk = []
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    if len(stk):
        answer = stk[:]
    else:
        answer = [-1]
    return answer