# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 1e9

    if len(s) == 1:
        return 1

    trimLen = len(s) // 2

    while trimLen > 0:
        tempStr = ""
        prevStr = ""
        nextStr = ""
        repeatCnt = 1

        for i in range(0, len(s), trimLen):
            nextStr = s[i : i + trimLen]
            if prevStr == "":
                prevStr = nextStr
                continue
            if prevStr == nextStr:
                repeatCnt += 1
            else:
                if repeatCnt > 1:
                    tempStr += str(repeatCnt) + prevStr
                else:
                    tempStr += prevStr
                repeatCnt = 1
                prevStr = nextStr

        if repeatCnt > 1:
            tempStr += str(repeatCnt) + prevStr
        else:
            tempStr += prevStr
        trimLen -= 1

        if answer > len(tempStr):
            answer = len(tempStr)

    return answer

# result = solution("aabbaccc")
# result = solution("ababcdcdababcdcd")
result = solution("abcabcabcabcdededededede")
print("result", result)
