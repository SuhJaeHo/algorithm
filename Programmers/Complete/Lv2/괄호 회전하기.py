# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    cnt = 0

    bracketPair = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    while cnt < len(s):
        cnt += 1
        s = s[1:] + s[:1]

        flag = True
        stack = []

        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            else:
                if len(stack) == 0 or bracketPair[bracket] != stack.pop():
                    flag = False
                    break

        if len(stack) != 0:
            flag = False

        if flag:
            answer += 1

    return answer

result = solution("[](){}")
print("result", result)
