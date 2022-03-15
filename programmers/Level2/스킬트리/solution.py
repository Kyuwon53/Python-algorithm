def solution(skill, skill_trees):
    answer = 0
    skill_pattern = []
    for s in range(len(skill)):
        skill_pattern.append(skill[0:s + 1])

    for skill_tree in skill_trees:
        contains_skill = ""
        for current_skill in skill_tree:
            nums = 0
            if current_skill in skill:
                contains_skill += current_skill

            if contains_skill in skill_pattern:
                nums += 1
                print(skill_tree, contains_skill, current_skill)

        if len(contains_skill) == 0:
            nums += 1

        if nums > 0:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["C", "D", "CB", "BDA"]

print(solution(skill, skill_trees))
