# 게임 맵 최단거리 (https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3)
from collections import deque

def solution(maps):

    dq = deque([[0, 0, 0]]) # x좌표, y좌표, 이동수
    visited = set()
    visited.add((0, 0))
    answer = -1

    while dq:

        x, y, steps = dq.popleft()

        # 위로 이동
        if y - 1 >= 0:
            if maps[y - 1][x] == 1 and (x, y - 1) not in visited:
                dq.append([x, y - 1, steps + 1])
                visited.add((x, y - 1))

        # 아래로 이동
        if y + 1 < len(maps):
            if x == len(maps[0]) - 1 and y + 1 == len(maps) - 1:
                answer = steps + 1
                break
            elif maps[y + 1][x] == 1 and (x, y + 1) not in visited:
                dq.append([x, y + 1, steps + 1])
                visited.add((x, y + 1))

        # 왼쪽으로 이동
        if x - 1 >= 0:
            if maps[y][x - 1] == 1 and (x - 1, y) not in visited:
                dq.append([x - 1, y, steps + 1])
                visited.add((x - 1, y))

        # 오른쪽으로 이동
        if x + 1 < len(maps[0]):
            if x + 1 == len(maps[0]) - 1 and y == len(maps) - 1:
                answer = steps + 1
                break
            elif maps[y][x + 1] == 1 and (x + 1, y) not in visited:
                dq.append([x + 1, y, steps + 1])
                visited.add((x + 1, y))

    return answer + 1 if answer > 0 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))