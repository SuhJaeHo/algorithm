# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    skill_orders_dict = {}
    for item in skill:
        skill_orders_dict[item] = 1

    for skill_tree in skill_trees:
        flag = True
        skill_orders_list = list(skill)
        for skill_item in skill_tree:
            if skill_orders_dict.get(skill_item):
                if skill_orders_list[0] != skill_item:
                    flag = False
                    break
                else:
                    skill_orders_list.pop(0)

        if flag:
            answer += 1

    return answer

result = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
print("result", result)
