def solution(myStr):
    answer = []
    
    string = ''
    for i in range(len(myStr)):
        if myStr[i] == 'a' or myStr[i] == 'b' or myStr[i] == 'c':
            if len(string) != 0:
                answer.append(string)
                string = ''
        else:
            string = string + myStr[i]
        if i == len(myStr)-1 and len(string) !=0:
            answer.append(string)
    if len(answer) == 0:
        answer.append('EMPTY')
    return answer