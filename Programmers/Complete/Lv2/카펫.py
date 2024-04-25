# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []

    width = brown + yellow

    half = width // 2
    for i in range(1, half):
        if (i * 2) + ((width / i) * 2) - 4 == brown:
            if i >= int(width / i):
                answer.append(i)
                answer.append(int(width / i))
            else:
                answer.append(int(width / i))
                answer.append(i)
            return answer

    return answer

# result = solution(10, 2)
# result = solution(8, 1)
result = solution(24, 24)
print("result", result)
