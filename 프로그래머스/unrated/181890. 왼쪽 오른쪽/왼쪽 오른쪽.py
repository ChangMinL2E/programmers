def solution(str_list):
    answer = []
    l_idx, r_idx = 21,21
    if 'l' in str_list:
        l_idx = str_list.index('l')
    if 'r' in str_list:
        r_idx = str_list.index('r')
    
    if l_idx != r_idx:
        if l_idx < r_idx:
            answer = str_list[:l_idx]
        else:
            answer = str_list[r_idx+1:]
    
    return answer