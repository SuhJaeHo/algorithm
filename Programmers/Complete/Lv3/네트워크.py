# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def dfs(computers, visited, currIdx):
    visited[currIdx] = True

    for i in range(len(computers)):
        if computers[currIdx][i] == 1 and not visited[i]:
            dfs(computers, visited, i)


def solution(n, computers):
    answer = 0

    visited = [False] * n
    print(visited)

    for i in range(len(computers)):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1

    return answer

result = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# result = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
print("result", result)
