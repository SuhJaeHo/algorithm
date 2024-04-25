# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    chars = ["A", "E", "I", "O", "U"]

    def dfs(str, acc):
        if str == word:
            return acc[0]

        if len(str) == len(chars):
            return

        for char in chars:
            str += char
            acc[0] += 1
            flag = dfs(str, acc)

            if flag is not None:
                return acc[0]

            str = str[:-1]

    answer = dfs("", [0])
    return answer

# result = solution("AAAAE")
result = solution("I")
print("result", result)
