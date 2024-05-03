# https://school.programmers.co.kr/learn/courses/30/lessons/12952

def check(n, table, row, col):
    for i in range(1, n):
        if table[row][i] == "Q" or table[i][col] == "Q":
            return False
        nRow = [1, 0, -1, 0, 1, -1, 1, -1]
        nCol = [0, 1, 0, -1, 1, -1, -1, 1]
        for j in range(8):
            dRow = row + i * nRow[j]
            dCol = col + i * nCol[j]
            if dRow >= 0 and dRow < n and dCol >= 0 and dCol < n:
                if table[dRow][dCol] == "Q":
                    return False
    return True

def dfs(n, table, row):
    acc = 0

    if row == n:
        return 1
    else:
        for col in range(n):
            flag = check(n, table, row, col)
            if flag:
                table[row][col] = "Q"
                acc += dfs(n, table, row + 1)
                table[row][col] = 0

    return acc

def solution(n):
    answer = 0

    table = [[0] * n for _ in range(n)]
    row = 0

    answer = dfs(n, table, row)
    return answer

result = solution(4)
print("result", result)
