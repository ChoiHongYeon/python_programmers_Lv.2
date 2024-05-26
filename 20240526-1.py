# 연속된 부분 수열의 합 (https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=python3)

def solution(sequence, k):
    
    len_min = (int) (k / sequence[len(sequence) - 1])
    result_len = 0
    result_index = 0

    for i in range(len_min, len(sequence) + 1):
        for j in range(len(sequence) - 1, i - 2, -1):
            if sum(sequence[j : j - i : -1]) == k:
                result_len = i
                result_index = j
                break
            elif sum(sequence[j : j - i : -1]) < k:
                break
        if result_len != 0:
            break
    
    answer = []
    if sequence[result_index] == sequence[result_index - result_len + 1]:
        answer.append(sequence.index(sequence[result_index]))
        answer.append(sequence.index(sequence[result_index]) + result_len - 1)
    else:
        answer.append(result_index - result_len + 1)
        answer.append(result_index)
    
    return answer

result1 = solution([1, 2, 3, 4, 5], 7)
result2 = solution([1, 1, 1, 2, 3, 4, 5], 5)
result3 = solution([2, 2, 2, 2, 2], 6)

print(result1, result2, result3)