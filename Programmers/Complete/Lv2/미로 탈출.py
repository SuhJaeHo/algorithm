# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def bfs(maps, target, row, col):
    queue = deque()
    queue.append([row, col, 1])

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[row][col] = True

    while queue:
        [row, col, acc] = queue.popleft()

        dRow = [1, 0, -1, 0]
        dCol = [0, 1, 0, -1]

        for i in range(4):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if nRow >= 0 and nRow < len(maps) and nCol >= 0 and nCol < len(maps[0]) and maps[nRow][nCol] != "X":
                if maps[nRow][nCol] == target:
                    return [True, acc, nRow, nCol]
                if not visited[nRow][nCol]:
                    visited[nRow][nCol] = True
                    queue.append([nRow, nCol, acc + 1])

    return [False, 0, 0, 0]

def solution(maps):
    answer = 0

    rows = len(maps)
    cols = len(maps[0])

    for row in range(rows):
        for col in range(cols):
            if maps[row][col] == "S":
                [isFind, acc, row, col] = bfs(maps, "L", row, col)
                if not isFind:
                    return -1
                answer += acc
                [isFind, acc, row, col] = bfs(maps, "E", row, col)
                if not isFind:
                    return -1
                answer += acc
                return answer

    return answer

result = solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])
# result = solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])
print("result", result)
