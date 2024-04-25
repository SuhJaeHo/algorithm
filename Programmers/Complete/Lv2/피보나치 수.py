# https://school.programmers.co.kr/learn/courses/30/lessons/12945

# def solution(n):
#     dp = [0] * (n + 1)
#     dp[1] = 1

#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n] % 1234567

def solution(n):
    memo = [0] * (n + 1)

    def fibonacci(n, memo):
        if n == 0 or n == 1:
            return n

        if memo[n] != 0:
            return memo[n]

        acc = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = acc

        return acc

    answer = fibonacci(n, memo)
    return answer % 1234567

# result = solution(3)
result = solution(5)
print("result", result)
