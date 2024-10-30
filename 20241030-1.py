# 예상 대진표 (https://school.programmers.co.kr/learn/courses/30/lessons/12985?language=python3)

def solution(n,a,b):

    answer = 0
    d = 2

    while True:
        answer += 1
        if (a - 1) // d == (b - 1) // d:
            break
        d *= 2

    return answer

print(solution(8, 4, 7))