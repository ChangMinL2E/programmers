def solution(arr):
    answer = list(map(test,arr))
    return answer

def test(num):
    if num >=50 and not num%2:
        return num//2
    elif num < 50 and num%2:
        return num*2
    else:
        return num