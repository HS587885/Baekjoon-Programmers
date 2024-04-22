from collections import Counter

def solution(k, tangerine):
    size_memo = sorted(Counter(tangerine).items(), key=lambda item: item[1], reverse =True)
    total = 0
    cnt = 0
    for i in range(len(size_memo)):
        total += size_memo[i][1]
        cnt += 1
        if total >= k:
            return cnt
