# https://school.programmers.co.kr/learn/courses/30/lessons/152996

def solution(users, emoticons):
    answer = []

    discountRatios = [10, 20, 30, 40]
    discounts = []

    def dfs(items):
        if len(items) == len(emoticons):
            items = items[:]
            discounts.append(items)
            return

        for i in range(len(discountRatios)):
            items.append(discountRatios[i])
            dfs(items)
            items.pop()

    dfs([])

    for i in range(len(discounts)):
        cost = 0
        cnt = 0
        for user in users:
            tmpCost = 0
            for j in range(len(emoticons)):
                if discounts[i][j] >= user[0]:
                    tmpCost += emoticons[j] * ((100 - discounts[i][j]) / 100)

            if tmpCost >= user[1]:
                cnt += 1
            else:
                cost += tmpCost

        answer.append([cnt, cost])

    answer.sort(key = lambda x: (-x[0], -x[1]))
    return answer[0]

result = solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
print("result", result)
