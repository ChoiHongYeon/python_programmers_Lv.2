# 당구 연습 (https://school.programmers.co.kr/learn/courses/30/lessons/169198)
import math

def solution(m, n, startX, startY, balls):
    
    answer = []

    for i in balls:
        j = []
        # 위로 칠 때(top)
        if startX == i[0]:
            if startY > i[1]:
                top = ((n - startY) + (n - i[1])) ** 2
                j.append(top)
        else:
            h1 = n - startY
            h2 = n - i[1]
            w1 = h1 * abs(i[0] - startX) / (h1 + h2)
            w2 = abs(i[0] - startX) - w1
            top = round((math.sqrt(w1 ** 2 + h1 ** 2) + math.sqrt(w2 ** 2 + h2 ** 2)) ** 2)
            j.append(top)
        # 아래로 칠 때(bottom)
        if startX == i[0]:
            if startY < i[1]:
                bottom = (startY + i[1]) ** 2
                j.append(bottom)
        else:
            w1 = startY * abs(i[0] - startX) / (startY + i[1])
            w2 = abs(i[0] - startX) - w1
            bottom = round((math.sqrt(w1 ** 2 + startY ** 2) + math.sqrt(w2 ** 2 + i[1] ** 2)) ** 2)
            j.append(bottom)
        # 오른쪽으로 칠 때(right)
        if startY == i[1]:
            if startX > i[0]:
                right = ((m - startX) + (m - i[0])) ** 2
                j.append(right)
        else:
            w1 = m - startX
            w2 = m - i[0]
            h1 = w1 * abs(i[1] - startY) / (w1 + w2)
            h2 = abs(i[1] - startY) - h1
            right = round((math.sqrt(w1 ** 2 + h1 ** 2) + math.sqrt(w2 ** 2 + h2 ** 2)) ** 2)
            j.append(right)
        # 왼쪽으로 칠 때(left)
        if startY == i[1]:
            if startX < i[0]:
                left = (startX + i[0]) ** 2
                j.append(left)
        else:
            h1 = startX * abs(i[1] - startY) / (startX + i[0])
            h2 = abs(i[1] - startY) - h1
            left = round((math.sqrt(startX ** 2 + h1 ** 2) + math.sqrt(i[0] ** 2 + h2 ** 2)) ** 2)
            j.append(left)

        answer.append(min(j))
        
    return answer

result = solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]])
print(result)