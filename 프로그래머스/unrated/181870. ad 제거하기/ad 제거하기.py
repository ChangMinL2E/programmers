def solution(strArr):
    answer = []
    strArr2 = list(map(lambda x: 'ad' in x, strArr))
    for i in range(len(strArr2)):
        if not strArr2[i]:
            answer.append(strArr[i])
    return answer