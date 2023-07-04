def solution(num_list):
    answer = 0
    
    total1 = 1
    total2 = 0
    
    for num in num_list:
        total1 *= num
        total2 += num
    
    total2 = total2**2
    
    if total2 > total1:
        answer = 1
    
    return answer