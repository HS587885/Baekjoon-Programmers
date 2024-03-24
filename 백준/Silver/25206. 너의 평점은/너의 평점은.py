# 등급에 따른 과목평점을 저장하는 딕셔너리
grade_points = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

# 전공과목 수
num_subjects = 20

# 총 학점과 과목별 학점×과목평점을 저장할 변수 초기화
total_credits = 0
total_grade_points = 0

# 전공과목의 정보 입력 및 계산
for _ in range(num_subjects):
    subject, credit, grade = input().split()
    credit = float(credit)
    
    # P/F 과목은 제외
    if grade != 'P':
        total_credits += credit
        total_grade_points += credit * grade_points[grade]

# 전공평점 계산
if total_credits == 0:
    print("치훈이는 졸업할 수 없습니다.")
else:
    major_gpa = total_grade_points / total_credits
    print("%.6f" % major_gpa)
