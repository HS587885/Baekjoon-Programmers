def solution(skill, skill_trees):
    count = 0
    
    for tree in skill_trees:
        skill_index = 0
        is_valid = True
        
        for s in tree:
            if s in skill:
                if s == skill[skill_index]:
                    skill_index += 1
                else:
                    is_valid = False
                    break
        
        if is_valid:
            count += 1
    
    return count
