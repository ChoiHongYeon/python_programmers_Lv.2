# 연속된 부분 수열의 합 (https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=python3)

def solution(sequence, k):
    
    s = [sequence[len(sequence) - 1]]
    s_max, s_min = len(sequence) - 1, len(sequence) - 1
    
    while sum(s) != k:
        if sum(s) > k:
            s.pop()
            s_max -= 1
        else:
            s_min -= 1
            s.insert(0, sequence[s_min])

    if max(s) == min(s):
        return [sequence.index(s[0]), sequence.index(s[0]) + s_max - s_min]
    else:
        return [s_min, s_max]



result1 = solution([1, 2, 3, 4, 5], 7)
result2 = solution([1, 1, 1, 2, 3, 4, 5], 5)
result3 = solution([2, 2, 2, 2, 2], 6)

print(result1, result2, result3)