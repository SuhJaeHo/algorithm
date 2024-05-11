# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0

    parent = [0] * n
    parent = [i for i in range(n)]

    edges = []

    for i in range(len(costs)):
        a, b, cost = costs[i]
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer

result = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
print("result", result)
