# 두 원 사이의 정수 쌍

import math

def solution(a, b):
    
    a2 = a ** 2
    b2 = b ** 2

    z = ((b - a) + 1) * 4 # xy좌표 하나라도 0인 경우

    s = (int(math.sqrt((b ** 2) / 2)) - (int(math.sqrt((a ** 2) / 2) + 1)) + 1) * 4 # xy좌표 같은 경우

    o = 0
    for x in range(1, int(math.sqrt((b ** 2) / 2)) + 1):
        min_y = 0
        max_y = 0
        for y in range(x + 1, b):
            if x != y and (x ** 2) + (y ** 2) >= a2 and (x ** 2) + (y ** 2) <= b2:
                min_y = y
                break
        for y in range(b - 1, x, -1):
            if x != y and (x ** 2) + (y ** 2) >= a2 and (x ** 2) + (y ** 2) <= b2:
                max_y = y
                break
        if min_y != 0 and max_y != 0:
            o += (max_y - min_y + 1)
    o *= 8 # 그 외의 경우
    
    answer = z + s + o
    return answer

result = solution(2,4)
print(result)