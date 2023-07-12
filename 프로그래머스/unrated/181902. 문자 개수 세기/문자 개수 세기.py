def solution(my_string):
    answer = [0]*52
    for i in range(ord('A'),ord('Z')+1):
        answer[i-65] += my_string.count(chr(i))
    for i in range(ord('a'),ord('z')+1):
        answer[i-71] += my_string.count(chr(i))
    return answer