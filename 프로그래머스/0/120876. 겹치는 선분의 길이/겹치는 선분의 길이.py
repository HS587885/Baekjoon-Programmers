# def solution(lines):
   
#     line_map = [0] * 201  

#     for line in lines:
#         start, end = line
#         for i in range(start + 100, end + 100):
#             line_map[i] += 1

#     overlap_length = 0
#     for count in line_map:
#         if count > 1:
#             overlap_length += 1

#     return overlap_length

def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))