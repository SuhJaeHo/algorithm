# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def compareStr(currStr, comparison):
    charDict = {}
    for i in range(len(currStr)):
        if not charDict.get(currStr[i]):
            charDict[currStr[i]] = 1
        else:
            charDict[currStr[i]] += 1

    for i in range(len(currStr)):
        if charDict.get(comparison[i]) and charDict[comparison[i]] > 0:
            charDict[comparison[i]] -= 1

    if sum(charDict.values()) == 1:
        return True
    return False

def solution(begin, target, words):
    answer = 0

    checked = [False] * len(words)

    queue = deque()
    queue.append([begin, checked, 0])

    while queue:
        [currStr, checked, cnt] = queue.popleft()

        if currStr == target:
            return cnt

        for i in range(len(words)):
            flag = compareStr(currStr, words[i])
            if not checked[i] and flag:
                checked = checked[:]
                checked[i] = True
                queue.append([words[i], checked, cnt + 1])

    return answer

result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
# result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])

# result = solution("aab", "aba", ["abb", "aba"])
print("result", result)
