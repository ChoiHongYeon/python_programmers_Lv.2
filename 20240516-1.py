# 두 원 사이의 정수 쌍

def solution(a, b):
   
    a2 = pow(a, 2)
    b2 = pow(b, 2)
   
    z = ((b - a) + 1) * 4 # xy좌표 하나라도 0
   
    min_s = 0
    max_s = 0
    for i in range(1, b + 1):
        if pow(i, 2) * 2 >= a2 and pow(i, 2) * 2 <= b2:
            min_s = i
            break
    for i in range(b, 0, -1):
        if pow(i, 2) * 2 >= a2 and pow(i, 2) * 2 <= b2:
            max_s = i
            break
    s = (max_s - min_s + 1) * 4 # xy좌표 같음
   
    o = 0
    for i in range(1, b):
        for j in range(1, (int)((b + 1) / 2)):
            if i != j and pow(i, 2) + pow(j, 2) >= a2 and pow(i, 2) + pow(j, 2) <= b2:
                o += 1
    o *= 8
   
    answer = z + s + o
   
    return answer

print(solution(2,3))