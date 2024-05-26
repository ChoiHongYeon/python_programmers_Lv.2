# 연속된 부분 수열의 합 (https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=python3)

def solution(sequence, k):

    s = sequence[len(sequence) - 1]
    s_max_index, s_min_index = len(sequence) - 1, len(sequence) - 1

    while s != k:
        if s > k:
            s -= sequence[s_max_index]
            s_max_index -= 1
        else:
            s_min_index -= 1
            s += sequence[s_min_index]

    if sequence[s_min_index] == sequence[s_max_index]:
        return [sequence.index(sequence[s_max_index]), sequence.index(sequence[s_max_index]) + s_max_index - s_min_index]
    else:
        return [s_min_index, s_max_index]

result1 = solution([1, 2, 3, 4, 5], 7)
result2 = solution([1, 1, 1, 2, 3, 4, 5], 5)
result3 = solution([2, 2, 2, 2, 2], 6)

print(result1, result2, result3)