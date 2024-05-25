# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def getCrushList(board, row, col):
    crush_list = [(row, col)]
    dRow = [1, 0, 1]
    dCol = [0, 1, 1]

    for i in range(3):
        nRow = row + dRow[i]
        nCol = col + dCol[i]
        if nRow < len(board) and nCol < len(board[0]):
            if board[nRow][nCol] == board[row][col]:
                crush_list.append((nRow, nCol))

    return crush_list

def solution(m, n, board):
    answer = 0

    board_list = []
    for row in board:
        board_list.append(list(row))

    while True:
        crush_list = []

        for row in range(m):
            for col in range(n):
                if board_list[row][col] != 0:
                    if len(getCrushList(board_list, row, col)) == 4:
                        crush_list += getCrushList(board_list, row, col)

        if len(crush_list) == 0:
            break

        for item in crush_list:
            [row, col] = item
            board_list[row][col] = 0

        for col in range(n):
            for row in range(m - 1, 0, -1):
                if board_list[row][col] == 0:
                    copy_row = row - 1
                    while copy_row >= 0:
                        if board_list[copy_row][col] != 0:
                            board_list[row][col] = board_list[copy_row][col]
                            board_list[copy_row][col] = 0
                            break

                        copy_row -= 1

    for row in range(m):
        for col in range(n):
            if board_list[row][col] == 0:
                answer += 1

    return answer

result = solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
# result = solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
result = solution(8, 5, ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"])
print("result", result)
