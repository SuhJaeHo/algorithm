def check(n, table, row, col):
    for i in range(0, row):
        if table[i][col] == "Q":
            return False

        if col - (row - i) >= 0:
            if table[i][col - (row - i)] == "Q":
                return False
        if col + (row - i) < n:
            if table[i][col + (row - i)] == "Q":
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

    # table = [[0] * n] * n
    table = [[0] * n for _ in range(n)]

    answer = dfs(n, table, 0)

    return answer

result = solution(4)
print("result", result)
