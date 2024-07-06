# 뒤에 있는 큰 수 찾기 (https://school.programmers.co.kr/learn/courses/30/lessons/154539)

def solution(numbers):

    up = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            up.append(numbers[i + 1])

    answer = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            answer.append(numbers[i + 1])
            del(up[0])
        else:
            if len(up) > 0:
                for j in range(len(up)):
                    if up[j] > numbers[i]:
                        answer.append(up[j])
            else:
                answer.append(-1)
        if i + 1 > len(answer):
            answer.append(-1)

    answer.append(-1)

    return answer

result1 = solution([2, 3, 3, 5])
result2 = solution([9, 1, 5, 3, 6, 2])

print(result1)
print(result2)