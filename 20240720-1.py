# 미로 탈출 (https://school.programmers.co.kr/learn/courses/30/lessons/159993)
from collections import deque

def solution(maps):
    
    start = [0, 0]
    for i in range(len(maps)):
        if maps[i].find("S") >= 0:
            start[0] = maps[i].find("S")
            start[1] = i

    lever = deque([[start[0], start[1], 0]])
    visited = [[start[0], start[1]]]
    lever_time = -1

    while lever:
        x, y, steps = lever.popleft()

        if y - 1 >= 0:
            if maps[y - 1][x] == "L":
                lever_time = steps + 1
                break
            elif maps[y - 1][x] != "X" and [x, y - 1] not in visited:
                lever.append([x, y - 1, steps + 1])
                visited.append([x, y - 1])
        if y + 1 <= len(maps) - 1:
            if maps[y + 1][x] == "L":
                lever_time = steps + 1
                break
            elif maps[y + 1][x] != "X" and [x, y + 1] not in visited:
                lever.append([x, y + 1, steps + 1])
                visited.append([x, y + 1])
        if x - 1 >= 0:
            if maps[y][x - 1] == "L":
                lever_time = steps + 1
                break
            elif maps[y][x - 1] != "X" and [x - 1, y] not in visited:
                lever.append([x - 1, y, steps + 1])
                visited.append([x - 1, y])
        if x + 1 <= len(maps[0]) - 1:
            if maps[y][x + 1] == "L":
                lever_time = steps + 1
                break
            elif maps[y][x + 1] != "X" and [x + 1, y] not in visited:
                lever.append([x + 1, y, steps + 1])
                visited.append([x + 1, y])

    if lever_time == -1:
        return -1
    
    for i in range(len(maps)):
        if maps[i].find("L") >= 0:
            start[0] = maps[i].find("L")
            start[1] = i

    exit = deque([[start[0], start[1], 0]])
    visited = [[start[0], start[1]]]
    exit_time = -1

    while exit:
        x, y, steps = exit.popleft()

        if y - 1 >= 0:
            if maps[y - 1][x] == "E":
                exit_time = steps + 1
                break
            elif maps[y - 1][x] != "X" and [x, y - 1] not in visited:
                exit.append([x, y - 1, steps + 1])
                visited.append([x, y - 1])
        if y + 1 <= len(maps) - 1:
            if maps[y + 1][x] == "E":
                exit_time = steps + 1
                break
            elif maps[y + 1][x] != "X" and [x, y + 1] not in visited:
                exit.append([x, y + 1, steps + 1])
                visited.append([x, y + 1])
        if x - 1 >= 0:
            if maps[y][x - 1] == "E":
                exit_time = steps + 1
                break
            elif maps[y][x - 1] != "X" and [x - 1, y] not in visited:
                exit.append([x - 1, y, steps + 1])
                visited.append([x - 1, y])
        if x + 1 <= len(maps[0]) - 1:
            if maps[y][x + 1] == "E":
                exit_time = steps + 1
                break
            elif maps[y][x + 1] != "X" and [x + 1, y] not in visited:
                exit.append([x + 1, y, steps + 1])
                visited.append([x + 1, y])

    if exit_time == -1:
        return -1
    else:
        return lever_time + exit_time

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))