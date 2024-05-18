# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = 0
    combs = {}

    cnt = 1
    tmpElements = elements + elements

    while cnt <= len(elements):
        for curr in range(len(elements)):
            comb = sum(tmpElements[curr : curr + cnt])
            if not combs.get(comb):
                combs[comb] = 1
        cnt += 1

    answer = len(combs.keys())
    return answer

result = solution([7,9,1,1,4])
print("result", result)
