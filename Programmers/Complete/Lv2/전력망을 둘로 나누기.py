# https://school.programmers.co.kr/learn/courses/30/lessons/86971

def dfs(point, connectPointsInfo, visited, exclude):
    acc = 1
    visited[point] = True
    [a, b] = exclude

    nextPointList = connectPointsInfo[point]

    for nextPoint in nextPointList:
        if not visited[nextPoint]:
            if not ((point == a and nextPoint == b) or (point == b and nextPoint == a)):
                acc += dfs(nextPoint, connectPointsInfo, visited, exclude)

    return acc

def solution(n, wires):
    answer = 1e9

    connectPointsInfo = {}
    for wire in wires:
        [a, b] = wire
        if not connectPointsInfo.get(a):
            connectPointsInfo[a] = [b]
        else:
            connectPointsInfo[a].append(b)
        if not connectPointsInfo.get(b):
            connectPointsInfo[b] = [a]
        else:
            connectPointsInfo[b].append(a)

    currIdx = 0
    while currIdx <= len(wires) - 1:
        visited = [False] * (n + 1)
        exclude = wires[currIdx]
        subAnswer = []

        for i in range(1, n + 1):
            if not visited[i]:
                acc = dfs(i, connectPointsInfo, visited, exclude)
                subAnswer.append(acc)

        if answer > abs(subAnswer[0] - subAnswer[1]):
            answer = abs(subAnswer[0] - subAnswer[1])

        currIdx += 1

    return answer

result = solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
# result = solution(4, [[1,2],[2,3],[3,4]])
print("result", result)
