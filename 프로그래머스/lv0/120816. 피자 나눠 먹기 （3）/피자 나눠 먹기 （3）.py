def solution(slice, n):
    answer = 0
    if not (n%slice):
        answer = n//slice
    else:
        answer = n//slice +1
    return answer