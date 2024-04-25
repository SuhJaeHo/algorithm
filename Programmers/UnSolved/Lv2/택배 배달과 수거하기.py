# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0

    acc = cap
    distanceList = []

    for i in range(n - 1, -1, -1):
        if deliveries[i] == 0:
            continue

        if acc == 0 or len(distanceList) == 0:
            acc = cap
            distanceList.append(i + 1)

        if acc >= deliveries[i]:
            acc -= deliveries[i]
        else:
            deliveries[i] -= acc
            for i in range((deliveries[i] // cap)):
                deliveries[i] -= cap
                distanceList.append(i + 1)
            if deliveries[i] % cap != 0:
                distanceList.append(i + 1)
                acc = cap - deliveries[i]

    for distance in distanceList:
        answer += distance * 2

    return answer

result = solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
# result = solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
print("result", result)

# def solution(cap, n, deliveries, pickups):
#     result = 0

#     deliveries = deliveries[::-1]
#     pickups = pickups[::-1]

#     leftDeliver = 0
#     leftPickups = 0

#     for i in range(n):
#         leftDeliver += deliveries[i]
#         leftPickups += pickups[i]

#         while leftDeliver > 0 or leftPickups > 0:
#             leftDeliver -= cap
#             leftPickups -= cap
#             result += (n - i) * 2

#     return result
