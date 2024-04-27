# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def my_solution(prices):
    answer = [0] * len(prices)

    stack = []
    for i in range(len(prices)):
        idx = len(stack) - 1

        while idx >= 0:
            [val, currIdx] = stack[idx]
            if val > prices[i]:
                answer[currIdx] = i - currIdx
                stack.pop()
            idx -= 1

        stack.append([prices[i], i])

    for item in stack:
        [_, idx] = item
        answer[idx] = len(prices) - 1 - idx

    return answer

def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        second = 0
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                second += 1
            else:
                break
        answer.append(second)

    answer.append(0)
    return answer

# result = solution([1, 2, 3, 2, 3])
result = solution([4, 3, 2, 1])
print("result", result)
