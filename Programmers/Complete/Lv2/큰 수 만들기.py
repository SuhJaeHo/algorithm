# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    return "".join(answer[:len(answer) - k])

# result = solution("1924", 2)
# result = solution("4177252841", 4)

result = solution("9876543214", 4)
print("result", result)
