# 다음 큰 숫자 (https://school.programmers.co.kr/learn/courses/30/lessons/12911?language=python3)

def solution(n):

    answer = n + 1
    while True:
        if bin(n)[2:].count('1') == bin(answer)[2:].count('1'):
            break
        answer += 1

    return answer

print(solution(78))
print(solution(15))