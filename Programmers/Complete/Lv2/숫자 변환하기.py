# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    answer = -1

    queue = deque()
    queue.append([x, 0])

    memo = {}

    while queue:
        [val, cnt] = queue.popleft()

        if val == y:
            answer = cnt
            break

        if val + n <= y:
            if not memo.get(val + n):
                memo[val + n] = True
                queue.append([val + n, cnt + 1])
        if val * 2 <= y:
            if not memo.get(val * 2):
                memo[val * 2] = True
                queue.append([val * 2, cnt + 1])
        if val * 3 <= y:
            if not memo.get(val * 3):
                memo[val * 3] = True
                queue.append([val * 3, cnt + 1])

    return answer

result = solution(10, 40, 5)
# result = solution(2, 5, 4)
print("result", result)
