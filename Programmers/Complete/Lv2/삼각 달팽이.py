# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []

    tmp_list = []
    for i in range(1, n + 1):
        tmp_list.append([0] * i)

    currIdx = 0
    currVal = 1

    lastRow = n
    initRow = 0

    while lastRow >= initRow:
        # down
        for row in range(initRow, lastRow):
            tmp_list[row][currIdx] = currVal
            currVal += 1

            if row == lastRow - 1:
                # left
                for col in range(currIdx + 1, len(tmp_list[row]) - currIdx):
                    tmp_list[row][col] = currVal
                    currVal += 1

                    # up
                    if col == len(tmp_list[row]) - 1 - currIdx:
                        for i in range(row - 1, initRow, -1):
                            tmp_list[i][len(tmp_list[i]) - 1 - currIdx] = currVal
                            currVal += 1
        currIdx += 1
        lastRow -= 1
        initRow += 2

    for i in range(n):
        for j in range(len(tmp_list[i])):
            answer.append(tmp_list[i][j])

    return answer

# result = solution(4)
# result = solution(5)
result = solution(6)
print("result", result)
