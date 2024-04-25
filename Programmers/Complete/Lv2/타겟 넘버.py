# https://school.programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    answer = 0

    subVal = (sum(numbers) - target) // 2

    queue = deque()
    if subVal >= numbers[0]:
        queue.append([1, numbers[0]])
    queue.append([1, 0])

    while queue:
        [idx, acc] = queue.popleft()
        if acc == subVal:
            answer += 1
            continue

        if idx <= len(numbers) - 1:
            if subVal >= numbers[idx]:
                queue.append([idx + 1, acc + numbers[idx]])
            queue.append([idx + 1, acc])

    return answer

# result = solution([1, 1, 1, 1, 1], 3)
result = solution([4, 1, 2, 1], 4)
print("result", result)
