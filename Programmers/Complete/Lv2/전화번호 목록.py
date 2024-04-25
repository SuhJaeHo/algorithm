# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# https://school.programmers.co.kr/questions/45470

def solution(phone_book):
    answer = True

    prefixes = {}

    for number in phone_book:
        if prefixes.get(number):
            return False
        else:
            prefixes[number] = 0

    for prefix in prefixes.keys():
        for number in phone_book:
            if number != prefix and number[:len(prefix)] == prefix:
                return False

    return answer

result = solution(["119", "97674223", "1195524421"])
print("result", result)
