def solution(num_list):
    answer = 0
    lst = [0]*31

    for i in range(2,31):
        if i%2:
            lst[i] = lst[(i-1)//2]+1
        else:
            lst[i] = lst[i//2]+1

    for num in num_list:
        answer+= lst[num]
    
    return answer