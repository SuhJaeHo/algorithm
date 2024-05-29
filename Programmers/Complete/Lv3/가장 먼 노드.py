# https://school.programmers.co.kr/learn/courses/30/lessons/49189

import heapq

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, edge):
    answer = 0
    INF = 1e9

    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

    for route in edge:
        [a, b] = route
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dijkstra(1, graph, distance)

    distance.sort(reverse = True)

    tmp = 0
    for i in range(1, len(distance)):
        if distance[i] >= tmp:
            tmp = distance[i]
            answer += 1
        else:
            break

    return answer

result = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print("result", result)
