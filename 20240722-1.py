# 무인도 여행 (https://school.programmers.co.kr/learn/courses/30/lessons/154540?language=python3)
import sys
sys.setrecursionlimit(10000)

def solution(maps):

    visited = [[False for i in range(len(maps[0]))] for i in range(len(maps))]
    move_x = [0, 0, -1, 1]
    move_y = [-1, 1, 0, 0]
    global island
    island = 0

    def DFS(x, y):

        if visited[y][x] == True:
            return 0
        visited[y][x] = True

        global island
        island += int(maps[y][x])

        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if (0 <= next_x < len(maps[0])) and (0 <= next_y < len(maps)) and (maps[next_y][next_x] != 'X'):
                DFS(next_x, next_y)

    answer = []
    for i in range(len(maps[0])):
        for j in range(len(maps)):
            if maps[j][i] != 'X' and not visited[j][i]:
                DFS(i, j)
                answer.append(island)
                island = 0

    if answer == []:
        return [-1]
    answer.sort()
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))