def solution(n):
    answer = 0

    number = str(n)
    for num in number:
        answer += int(num)

    return answer