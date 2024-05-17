# https://school.programmers.co.kr/learn/courses/30/lessons/132266

# def solution(n, roads, sources, destination):
#     answer = []

#     INF = 1e9
#     graph = [[INF] * (n + 1) for _ in range(n + 1)]

#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             if a == b:
#                 graph[a][b] = 0

#     for road in roads:
#         [a, b] = road
#         graph[a][b] = 1
#         graph[b][a] = 1

#     for k in range(1, n + 1):
#         for a in range(1, n + 1):
#             for b in range(1, n + 1):
#                 graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#                 # graph[b][a] = min(graph[b][a], graph[a][k] + graph[k][b])

#     routes = []
#     for source in sources:
#         routes.append([source, destination])

#     for route in routes:
#         [a, b] = route
#         dist = graph[a][b]

#         if dist == INF:
#             dist = -1
#         answer.append(dist)

#     return answer

# def solution(n, roads, sources, destination):
#     answer = [-1] * len(sources)

#     queue = deque()
#     queue.append([destination, 0])

#     graph = [[-1] * (n + 1) for _ in range(n + 1)]
#     for road in roads:
#         [a, b] = road
#         graph[a][b] = 1
#         graph[b][a] = 1

#     for i in range(len(sources)):
#         if sources[i] == destination:
#             answer[i] = 0

#     visited = [False] * (n + 1)
#     visited[destination] = True

#     while queue:
#         [curr, dist] = queue.popleft()

#         for i in range(len(sources)):
#             if graph[curr][sources[i]] == 1 and answer[i] == -1:
#                 answer[i] = dist + 1

#         for i in range(1, n + 1):
#             if graph[curr][i] != -1:
#                 if not visited[i]:
#                     visited[i] = True
#                     queue.append([i, dist + 1])

#     return answer

from collections import deque

def solution(n, roads, sources, destination):
    answer = []

    queue = deque()
    queue.append([destination, 0])

    graph = [[] for _ in range(n + 1)]
    for road in roads:
        [a, b] = road
        graph[a].append(b)
        graph[b].append(a)

    distances = [-1] * (n + 1)
    distances[destination] = 0

    visited = [False] * (n + 1)
    visited[destination] = True

    while queue:
        [curr, dist] = queue.popleft()

        for next in graph[curr]:
            if distances[next] == -1:
                queue.append([next, dist + 1])
                distances[next] = dist + 1

    for source in sources:
        answer.append(distances[source])

    return answer

# result = solution(3, [[1, 2], [2, 3]], [2, 3], 1)
result = solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)
print("result", result)
