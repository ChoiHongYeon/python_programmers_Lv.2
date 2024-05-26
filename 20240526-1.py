# 연속된 부분 수열의 합 (https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=python3)

def solution(sequence, k):

    for i in range(len(sequence) - 1, -1, -1):
        j = i
        s = 0
        while j >= 0 and s < k:
            s += sequence[j]
            j -= 1
        if s == k:
            break

    if sequence[j + 1] == sequence[i]:
        return [sequence.index(sequence[i]), sequence.index(sequence[i]) + i - j - 1]
    else:
        return [j + 1, i]


result1 = solution([1, 2, 3, 4, 5], 7)
result2 = solution([1, 1, 1, 2, 3, 4, 5], 5)
result3 = solution([2, 2, 2, 2, 2], 6)

print(result1, result2, result3)