import itertools

def solution(l, r):
    answer = []
    print(len(str(r)))
    permutations_lst = list(itertools.product(["0","5"],repeat = len(str(r))))
    permutations_lst= list(map(lambda x: int(''.join(x)),permutations_lst))
    answer = list(filter(lambda x: l<= x<= r, permutations_lst))
    if len(answer) == 0:
        answer = [-1]
    return answer