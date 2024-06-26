# https://school.programmers.co.kr/learn/courses/30/lessons/42860

# 1. 역행 했다가 순행하는 조건
# 2. 순행 했다가 역행하는 조건
# 3. 순행
# 4. 역행

def up_down(char):
    ini = ord("A")
    end = ord("Z")
    mid = ((ini + end) // 2)

    curr = ord(char)

    if curr > mid:
        return end - curr + 1

    return curr - ini

def solution(name):
    answer = 0

    idxList = []
    for i in range(len(name)):
        if name[i] != "A":
            idxList.append(i)

    # 변경할 문자가 없을 경우
    if len(idxList) == 0:
        return 0

    # 순행
    minMove = idxList[len(idxList) - 1]
    # 역행
    minMove = min(minMove, 1 + len(name) - 1 - idxList[0])

    maxGap = 0
    checkIdx = 0
    for i in range(len(idxList) - 1):
        if idxList[i + 1] - idxList[i] > maxGap:
            maxGap = idxList[i + 1] - idxList[i]
            checkIdx = idxList[i]

    filterIdxList = list(filter(lambda x: x > checkIdx, idxList))
    if maxGap != 1:
        # 순행 했다가 역행하는 조건
        minMove = min(minMove, (checkIdx * 2 + 1 + len(name) - 1 - filterIdxList[0]))
        # 역행 했다가 순행하는 조건
        minMove = min(minMove, 1 + (len(name) - 1 - filterIdxList[0]) * 2 + 1 + checkIdx)

    answer += minMove

    for char in name:
        answer += up_down(char)

    return answer

# result = solution("JEROEN")
# result = solution("JAN")

result = solution("AAAAAAAAABBBBB")
print("result", result)
