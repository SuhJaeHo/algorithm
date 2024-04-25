# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0

    for row in range(1, len(land)):
        for col in range(len(land[0])):
            land[row][col] = land[row][col] + max(land[row - 1][:col] + land[row - 1][col + 1:])

    answer = max(land[len(land) - 1])
    return answer

result = solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
print("result", result)
