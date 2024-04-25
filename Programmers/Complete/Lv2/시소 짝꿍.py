# https://school.programmers.co.kr/learn/courses/30/lessons/152996

def solution(weights):
    answer = 0

    ratios = [1, 2/3, 3/2, 3/4, 4/3, 2/4, 4/2]

    weightCnt = {}
    for weight in weights:
        if weightCnt.get(weight):
            weightCnt[weight] += 1
        else:
            weightCnt[weight] = 1

    for weight in weights:
        for ratio in ratios:
            pairWeight = weight * ratio
            if weightCnt.get(pairWeight):
                if pairWeight == weight:
                    answer += weightCnt[pairWeight] - 1
                else:
                    answer += weightCnt[pairWeight]

        weightCnt[weight] -= 1

    return answer

result = solution([100,180,360,100,270])
print("result", result)
