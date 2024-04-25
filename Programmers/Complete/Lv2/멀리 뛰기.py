# https://school.programmers.co.kr/learn/courses/30/lessons/12914

from collections import deque

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567

def mySolution(n):
    answer = 0

    queue = deque()

    jumps = [1, 2]
    for jump in jumps:
        if jump <= n:
            queue.append(jump)

    while queue:
        acc = queue.popleft()

        if acc == n:
            answer += 1
            continue

        for jump in jumps:
            if acc + jump <= n:
                queue.append(acc + jump)

    return answer % 1234567

result = solution(4)
print("result", result)
