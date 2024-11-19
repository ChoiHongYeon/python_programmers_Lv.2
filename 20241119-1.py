# 기능개발 (https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3)

def solution(progresses, speeds):

    answer = []
    a = 0

    while progresses:
        answer.append(0)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            if progresses[0] >= 100:
                del(progresses[0])
                answer[a] += 1
            else:
                break
        a += 1

    real_answer = []
    for i in answer:
        if i > 0:
            real_answer.append(i)

    return real_answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))