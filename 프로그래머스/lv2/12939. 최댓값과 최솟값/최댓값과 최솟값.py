def solution(s):
    answer = s.split(' ')
    answer = list(map(int, answer))
    answer = f"{str(min(answer))} {str(max(answer))}"
    return answer