def solution(dartResult):
    # "10"을 "A"로 치환하여 처리하기 쉽게 함
    dartResult = dartResult.replace("10", "A")
    # 점수 계산을 위한 규칙 정의
    score_rules = {'S': '**1', 'D': '**2', 'T': '**3', "*": "*", '#': '*(-1)'}
    total_score = 0
    score_str = ''
    
    # dartResult를 숫자와 연산자로 분리
    for char in dartResult:
        if char.isdigit() or char == 'A':
            if char == 'A':
                score_str += ' ' + '10'
            else:
                score_str += " " + char
        else:
            score_str += char
    
    # 공백을 기준으로 점수 단위 분리
    scores = score_str.split()
    
    # 옵션 처리 로직 간소화
    for i, score in enumerate(scores):
        if '*' in score:
            scores[i] = scores[i].replace('*', '*2')
            if i > 0:
                scores[i-1] += '*2'
    
    # 각 점수 계산 및 총합 업데이트
    for score in scores:
        calc_score = ''
        for char in score:
            calc_score += score_rules.get(char, char)
        total_score += eval(calc_score)
    
    return total_score
