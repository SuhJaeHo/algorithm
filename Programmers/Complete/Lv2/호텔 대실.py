# https://school.programmers.co.kr/learn/courses/30/lessons/155651

import heapq

def getTimeStamp(timeStr):
    times = [int(i) for i in timeStr.split(":")]
    return times[0] * 60 + times[1]

def solution(book_time):
    answer = 0

    heap = []
    book_time.sort(key = lambda x: x[0])

    heapq.heappush(heap, book_time[0][1])

    for i in range(1, len(book_time)):
        check_out = heap[0]
        if getTimeStamp(book_time[i][0]) - getTimeStamp(check_out) >= 10:
            heapq.heappop(heap)
        heapq.heappush(heap, book_time[i][1])

    answer = len(heap)
    return answer

result = solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
print("result", result)
