# 숫자 변환하기 (https://school.programmers.co.kr/learn/courses/30/lessons/154538)

from collections import deque

def solution(x, y, n):

    if x == y:
        return 0
    
    q = deque([[x, 0]])
    visited = set([x])

    while q:
        number, steps = q.popleft()

        for i in [number + n, number * 2, number * 3]:
            if i == y:
                return steps + 1
            if i < y and i not in visited:
                q.append([i, steps + 1])
                visited.add(i)

    return -1

result1 = solution(10, 40, 5)
result2 = solution(10, 40, 30)
result3 = solution(2, 5, 4)

print(result1, result2, result3)