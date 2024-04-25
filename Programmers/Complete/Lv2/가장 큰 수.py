# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ""

    strNumbers = [str(number) for number in numbers]
    strNumbers.sort(key = lambda x: x * 3, reverse = True)
    answer = str(int("".join(strNumbers)))
    return answer

# result = solution([6, 10, 2])
result = solution([3, 30, 34, 5, 9]	)
print("result", result)
