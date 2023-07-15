def solution(binomial):
    answer = binomial.split(' ')
    a,b = answer[0],answer[2]
    
    if answer[1] == '+':
        answer = int(a)+int(b)
    elif answer[1] == '-':
        answer = int(a)-int(b)
    else:
        answer = int(a)*int(b)
    return answer