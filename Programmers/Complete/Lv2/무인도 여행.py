# https://school.programmers.co.kr/learn/courses/30/lessons/154540

import sys
sys.setrecursionlimit(10000)

def dfs(maps, row, col):
    acc = int(maps[row][col])
    maps[row][col] = "X"

    dRow = [1, 0, -1, 0]
    dCol = [0, 1, 0, -1]

    for i in range(4):
        nRow = row + dRow[i]
        nCol = col + dCol[i]
        if nRow >= 0 and nRow < len(maps) and nCol >= 0 and nCol < len(maps[0]) and maps[nRow][nCol] != "X":
            acc += dfs(maps, nRow, nCol)

    return acc

def solution(maps):
    answer = []

    maps = [list(map) for map in maps]
    rows = len(maps)
    cols = len(maps[0])

    for row in range(rows):
        for col in range(cols):
            if maps[row][col] != "X":
                acc = dfs(maps, row, col)
                answer.append(acc)

    if len(answer) == 0:
        return [-1]

    answer.sort()
    return answer

result = solution(["X591X","X1X5X","X231X", "1XXX1"])
# result = solution(["11", "1X"])
# result = solution(["XXX","XXX","XXX"])
print("result", result)
