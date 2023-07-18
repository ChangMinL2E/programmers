def solution(picture, k):
    answer = picture[:]
    answer = list(map(lambda x: list(x), answer))
    for i in range(len(answer)):
        answer[i] = list(map(lambda x: x*k, answer[i]))
        answer[i] = ''.join(answer[i])
    
    sol = []
    for lst in answer:
        for _ in range(k):
            sol.append(lst)
    
    return sol