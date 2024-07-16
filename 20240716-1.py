# 시소 짝꿍 (https://school.programmers.co.kr/learn/courses/30/lessons/152996?language=python3)

def solution(weights):

    w = []
    answer = 0

    for i in range(1001):
        w.append(0)
    for i in range(len(weights)):
        w[weights[i]] += 1

    for i in range(100, len(w)):
        if w[i] > 0:
            if i * 2 <= 1000 and w[i * 2] > 0:
                answer += w[i] * w[i * 2]
            if i * 1.5 <= 1000 and (i * 1.5) % 1 == 0 and w[int(i * 1.5)] > 0:
                answer += w[i] * w[int(i * 1.5)]
            if i * 4 / 3 <= 1000 and (i * 4 / 3) % 1 == 0 and w[int(i * 4 / 3)] > 0:
                answer += w[i] * w[int(i * 4 / 3)]
        if w[i] > 1:
            answer += int(w[i] * (w[i] - 1) / 2)

    return answer

print(solution([100, 180, 360, 100, 270]))