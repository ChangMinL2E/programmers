def solution(num_list):
    answer = 0
    odd_total = 0
    even_total = 0
    for i in range(len(num_list)):
        if i%2:
            odd_total += num_list[i]
        else:
            even_total += num_list[i]
    answer = max(odd_total, even_total)
    return answer