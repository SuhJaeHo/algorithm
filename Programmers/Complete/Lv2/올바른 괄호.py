# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True

    stack = []
    for char in s:
        if char == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)

    if len(stack) > 0:
        return False

    return answer

# result = solution("()()")
# result = solution("(())()")
result = solution(")()(")
# result = solution("(()(")
print("result", result)
