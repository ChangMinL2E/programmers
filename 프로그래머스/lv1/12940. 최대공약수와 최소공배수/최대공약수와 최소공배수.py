

def solution(n, m):
    minimum = 1
    maximum = m
    
    for i in range(n,0,-1):
        if not(n % i) and not(m%i):
            minimum = i
            break
    
    for j in range(m, 1000001):
        if not(j%n) and not(j%m):
            maximum = j
            break
    
    
    answer = [minimum, maximum]
    return answer