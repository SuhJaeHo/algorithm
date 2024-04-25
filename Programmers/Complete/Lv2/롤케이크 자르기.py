# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    answer = 0

    sideA = {}
    sideB = {}

    for item in topping:
        if sideB.get(item):
            sideB[item] += 1
        else:
            sideB[item] = 1

    for item in topping:
        sideB[item] -= 1
        if sideB[item] == 0:
            del sideB[item]
        if not sideA.get(item):
            sideA[item] = 1

        if len(sideA.keys()) == len(sideB.keys()):
            answer += 1

    return answer

result = solution([1, 2, 1, 3, 1, 4, 1, 2])
print("result", result)
