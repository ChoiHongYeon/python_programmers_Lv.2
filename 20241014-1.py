# 카펫 (https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=python3)

def solution(brown, yellow):

    if yellow == 1:
        return [3, 3]

    answer = []
    
    for i in range(1, int(yellow / 2) + 1):
        if yellow % i == 0:
            if (i + 2) * (yellow / i + 2) - yellow == brown:
                answer.append(int(yellow / i + 2))
                answer.append(i + 2)
                break

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))