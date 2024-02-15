import re

def solution(park, routes):
    park_size_max = [len(park) - 1, len(list(park[-1])) - 1]
    annoying = []
    startpoint = None  

    for k in range(len(park)):
        lst = list(park[k])
        for z in range(len(lst)):
            if lst[z] == "S":
                startpoint = [k, z] 
            if lst[z] == "X":
                annoying.append([k, z])
    print(f'annoying :  {annoying}')
    print(f'startpoint :  {startpoint}')
    print(f'park_size_max :  {park_size_max}')
    if not annoying:  
        for i in routes:
            number = int(re.sub(r'[^0-9]', '', i))
            direction = re.findall('[A-Z]', i)[0]
            if direction == 'E' and startpoint[1] + number <= park_size_max[1]:
                startpoint[1] = startpoint[1] + number
            elif direction == 'W' and startpoint[1] - number >= 0:
                startpoint[1] = startpoint[1] - number
            elif direction == 'S' and startpoint[0] + number <= park_size_max[0]:
                startpoint[0] = startpoint[0] + number
            elif direction == 'N' and startpoint[0] - number >= 0:
                startpoint[0] = startpoint[0] - number
        return startpoint
    else:
        for i in routes:
            number = int(re.sub(r'[^0-9]', '', i))
            direction = re.findall('[A-Z]', i)[0]
            original_w = startpoint[1]
            original_h  = startpoint[0]
            
            if direction == 'E' and startpoint[1] + number <= park_size_max[1]:
                startpoint[1] = startpoint[1] + number
                for i in annoying:
                    if startpoint[0] == i[0] and startpoint[1] >= i[1] and original_w < i[1]:
                        startpoint[1] = startpoint[1] - number
                        
            elif direction == 'W' and startpoint[1] - number >= 0:
                startpoint[1] = startpoint[1] - number
                for i in annoying:
                    if startpoint[0] == i[0] and startpoint[1] <= i[1] and original_w > i[1]:
                        startpoint[1] = startpoint[1] + number
                        
            elif direction == 'S' and startpoint[0] + number <= park_size_max[0]:
                startpoint[0] = startpoint[0] + number
                for i in annoying:
                    if startpoint[1] == i[1] and startpoint[0] >= i[0] and original_h < i[0]:
                        startpoint[0] = startpoint[0] - number
            
        
            elif direction == 'N' and startpoint[0] - number >= 0:
                        startpoint[0] = startpoint[0] - number
                        for i in annoying:
                            if startpoint[1] == i[1] and startpoint[0] <= i[0] and original_h > i[0]:
                                startpoint[0] = startpoint[0] + number

        return startpoint