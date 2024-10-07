# 최댓값과 최솟값 (https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3)

def solution(s):

    ss = s.split(" ")
    sss = []

    for i in ss:
        sss.append(int(i))

    return str(min(sss)) + " " + str(max(sss))

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))