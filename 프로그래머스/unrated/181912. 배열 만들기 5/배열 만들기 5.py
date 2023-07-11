def solution(intStrs, k, s, l):
    answer = intStrs[:]
    answer = list(map(lambda x: x[s:s+l], answer))
    
    answer = list(map(int,(filter(lambda x: int(x) > k, answer))))
    
    
    
    return answer