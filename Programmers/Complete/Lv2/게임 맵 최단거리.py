# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    answer = -1

    queue = deque()
    queue.append([0, 0, 1])

    dRow = [1, 0, -1, 0]
    dCol = [0, 1, 0, -1]

    while queue:
        [row, col, cnt] = queue.popleft()

        if row == len(maps) - 1 and col == len(maps[0]) - 1:
            answer = cnt
            return answer

        for i in range(4):
            nRow = row + dRow[i]
            nCol = col + dCol[i]

            if nRow >= 0 and nRow < len(maps) and nCol >= 0 and nCol < len(maps[0]) and maps[nRow][nCol] == 1:
                maps[nRow][nCol] = 0
                queue.append([nRow, nCol, cnt + 1])

    return answer

result = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
# result = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
print("result", result)
