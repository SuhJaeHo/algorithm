# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    answer = 0

    types = {}
    for item in tangerine:
        if not types.get(item):
            types[item] = 1
        else:
            types[item] += 1

    cnts = sorted(list(types.values()), reverse = True)

    for cnt in cnts:
        k -= cnt
        answer += 1
        if k <= 0:
            break

    return answer

result = solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
print("result", result)
