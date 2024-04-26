# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def dfs(k, dungeons, visited, acc, cntList):
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            acc += 1
            k -= dungeons[i][1]
            visited[i] = True
            cnt = dfs(k, dungeons, visited, acc, cntList)
            if cnt > cntList[0]:
                cntList[0] = cnt

            acc -= 1
            k += dungeons[i][1]
            visited[i] = False

    return acc

def solution(k, dungeons):
    cntList = [0]
    visited = [False] * len(dungeons)

    dfs(k, dungeons, visited, 0, cntList)

    return cntList[0]

result = solution(80, [[80,20],[50,40],[30,10]])
# result = solution(80, [[80,20],[70,50],[30,10],[20,20]])
print("result", result)
