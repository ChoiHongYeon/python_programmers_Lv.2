# 과제 진행하기 (https://school.programmers.co.kr/learn/courses/30/lessons/176962?language=python3)

def solution(plans):
    
    answer = []
    remaining_work = []
    freetime = 0

    for i in range(len(plans)):
        P = plans[i][1].split(":")
        plans[i][1] = int(P[0]) * 60 + int(P[1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x : x[1])

    for i in range(len(plans) - 1):
        if plans[i][1] + plans[i][2] > plans[i + 1][1]:
            plans[i][2] -= (plans[i + 1][1] - plans[i][1])
            remaining_work.append(i)
        elif plans[i][1] + plans[i][2] == plans[i + 1][1]:
            answer.append(plans[i][0])
        else:
            answer.append(plans[i][0])
            freetime = plans[i + 1][1] - plans[i][1] - plans[i][2]
            while freetime > 0 and remaining_work != []:
                if freetime >= plans[max(remaining_work)][2]:
                    answer.append(plans[max(remaining_work)][0])
                    freetime -= plans[max(remaining_work)][2]
                    remaining_work.pop()
                else:
                    plans[max(remaining_work)][2] -= freetime
                    freetime=0

    answer.append(plans[len(plans) - 1][0])
    while remaining_work != []:
        answer.append(plans[max(remaining_work)][0])
        remaining_work.pop()

    return answer

plans1 = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
plans2 = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
plans3 = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
result1 = solution(plans1)
result2 = solution(plans2)
result3 = solution(plans3)
print(result1, result2, result3)
