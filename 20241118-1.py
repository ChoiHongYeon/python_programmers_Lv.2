# H-Index (https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3)

def solution(citations):

    h = len(citations)
    while h > 0:
        overH = 0
        for i in citations:
            if i >= h:
                overH += 1
        if overH >= h:
            break
        h -= 1

    return h

print(solution([3, 0, 6, 1, 5]))