def solution(price, money, count):
    payment = 0
    for i in range(count):
        payment += price * (i+1)

    answer = payment - money
    if answer < 0:
        answer = 0
    return answer