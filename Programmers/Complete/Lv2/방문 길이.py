# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def move(n, dir, point):
    xIdx = 0
    yIdx = 1

    if dir == "U":
        if point[yIdx] < n:
            point[yIdx] += 1
    elif dir == "D":
        if point[yIdx] > -n:
            point[yIdx] -= 1
    elif dir == "R":
        if point[xIdx] < n:
            point[xIdx] += 1
    else:
        if point[xIdx] > -n:
            point[xIdx] -= 1

    return point

def solution(dirs):
    answer = 0

    n = 5
    paths = {}

    point = [0, 0]

    for dir in dirs:
        [x1, y1] = point
        [x2, y2] = move(n, dir, point)

        if x1 == x2 and y1 == y2:
            continue

        path1 = "" + str(x1) + str(y1) + str(x2) + str(y2)
        path2 = "" + str(x2) + str(y2) + str(x1) + str(y1)

        if not paths.get(path1):
            answer += 1
            paths[path1] = 1
            paths[path2] = 1

    return answer

result = solution("ULURRDLLU")
# result = solution("LULLLLLLU")
print("result", result)
