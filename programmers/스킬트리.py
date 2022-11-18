def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        string_list = ["" for x in range(len(skill_tree))]
        for ele in skill:
            if ele in skill_tree:
                string_list[skill_tree.index(ele)] = ele
        
        if skill[:len("".join(string_list))] == "".join(string_list):
            answer += 1
    return answer