# 광물 캐기 (https://school.programmers.co.kr/learn/courses/30/lessons/172927?language=python3)
import math

def solution(picks, minerals):
    
    equipment = ["stone", "iron", "diamond"]
    work_time = min(sum(picks) * 5, len(minerals))
    change_time = math.ceil(work_time / 5)
    energy = []
    answer = 0

    for i in range(0, work_time, 5):
        e = 0
        if i + 4 > work_time - 1:
            for j in range(i, work_time):
                e += 5 ** equipment.index(minerals[j])
        else:
            for j in range(i, i + 5):
                e += 5 ** equipment.index(minerals[j])
        energy.append([e, int(i / 5)])

    energy.sort(key = lambda x : x[0], reverse = True)

    for i in range(change_time):
        if (energy[i][1] * 5) + 4 > work_time - 1:
            if picks[0] > 0:
                for j in range(energy[i][1] * 5, work_time):
                    answer += 1
                picks[0] -= 1
            elif picks[1] > 0:
                for j in range(energy[i][1] * 5, work_time):
                    if equipment.index(minerals[j]) == 2:
                        answer += 5
                    else:
                        answer += 1
                picks[1] -= 1
            else:
                for j in range(energy[i][1] * 5, work_time):
                    if equipment.index(minerals[j]) == 2:
                        answer += 25
                    elif equipment.index(minerals[j]) == 1:
                        answer += 5
                    else:
                        answer += 1
                picks[0] -= 1
        else:
            if picks[0] > 0:
                for j in range(energy[i][1] * 5, energy[i][1] * 5 + 5):
                    answer += 1
                picks[0] -= 1
            elif picks[1] > 0:
                for j in range(energy[i][1] * 5, energy[i][1] * 5 + 5):
                    if equipment.index(minerals[j]) == 2:
                        answer += 5
                    else:
                        answer += 1
                picks[1] -= 1
            else:
                for j in range(energy[i][1] * 5, energy[i][1] * 5 + 5):
                    if equipment.index(minerals[j]) == 2:
                        answer += 25
                    elif equipment.index(minerals[j]) == 1:
                        answer += 5
                    else:
                        answer += 1
                picks[0] -= 1

    return answer

result1 = solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
result2 = solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])

print(result1)
print(result2)