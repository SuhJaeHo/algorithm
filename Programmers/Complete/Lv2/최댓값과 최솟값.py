# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ""

    max = -1e9
    min = 1e9

    numList = list(map(int, s.split(" ")))

    for num in numList:
        if num >= max:
            max = num
        if num <= min:
            min = num

    answer += str(min)
    answer += " " + str(max)
    return answer

# result = solution("1 2 3 4")
result = solution("-1 -2 -3 -4")
print("result", result)
