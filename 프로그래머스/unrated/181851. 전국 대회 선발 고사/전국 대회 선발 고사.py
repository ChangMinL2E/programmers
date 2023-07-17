def solution(rank, attendance):
    answer = 0
    lst = rank[:]
    for i in range(len(rank)):
        # 등수, 인덱스
        lst[i] = (rank[i],i,attendance[i])
    
    lst = list(filter(lambda x: x[2], lst))
    lst = sorted(lst, key=lambda x: x[0])
    answer = 10000*lst[0][1]+100*lst[1][1]+lst[2][1]
    
    
    return answer