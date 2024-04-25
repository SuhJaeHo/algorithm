# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    curIdx = 0
    stack = []
    for i in range(1, len(order) + 1):
        if i != order[curIdx]:
            stack.append(i)
        else:
            curIdx += 1
            while stack and order[curIdx] == stack[-1]:
                stack.pop()
                curIdx += 1

    return curIdx

# result = solution([4, 3, 1, 2, 5])
# result = solution([5, 4, 3, 2, 1])

result = solution([4, 3, 5, 1, 2])
print("result", result)
