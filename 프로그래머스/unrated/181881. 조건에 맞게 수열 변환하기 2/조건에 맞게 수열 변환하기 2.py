def solution(arr):
    answer = 0
    pre_arr = []

    while pre_arr != arr:
        pre_arr = arr[:]
        arr = list(map(lambda x: lam(x), arr))
        
        answer += 1
        
    return answer-1

def lam(x):
    if x < 50 and x%2:
        return 2*x+1
    elif x >= 50 and not(x%2):
        return x/2
    else:
        return x