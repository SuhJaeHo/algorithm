# https://school.programmers.co.kr/learn/courses/30/lessons/152995

def solution(scores):
    answer = 0

    myScore = scores[0]
    tempList = []

    for i in range(1, len(scores)):
        if sum(scores[i]) > sum(myScore):
            if scores[i][0] > myScore[0] and scores[i][1] > myScore[1]:
                return -1
            tempList.append(scores[i])
            answer += 1

    tempList.sort(key = lambda x: (x[0], -x[1]), reverse = True)
    print(tempList)

    return answer

result = solution([[2,2],[1,4],[3,2],[3,2],[2,1]])
print("result", result)
