# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = []

    departures = {}
    for i in range(len(tickets)):
        if departures.get(tickets[i][0]):
            departures[tickets[i][0]].append(i)
        else:
            departures[tickets[i][0]] = [i]

    visited = [False] * len(tickets)

    def dfs(depart, route):
        if len(route) == len(tickets):
            for idx in departures[depart]:
                if not visited[idx]:
                    answer.append(route + [tickets[idx][1]])
            return

        if not departures.get(depart):
            return

        idxList = departures[depart]
        for idx in idxList:
            if not visited[idx]:
                visited[idx] = True
                dfs(tickets[idx][1], route + [tickets[idx][1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]

# result = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
result = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print("result", result)
