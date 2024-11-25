# 튜플 (https://school.programmers.co.kr/learn/courses/30/lessons/64065?language=python3)

def solution(s):

    ss = s.split("},{")
    ss[0] = ss[0][2:]
    ss[-1] = ss[-1][:len(ss[-1]) - 2]
    ss.sort(key = lambda x : len(x))
    
    sss = []
    for i in ss:
        sss += i.split(",")
    sss.sort()

    answer = [0] * len(ss[-1].split(","))
    n = 0
    for i in range(len(sss)):
        n += 1
        if i == len(sss) - 1 or sss[i] != sss[i + 1]:
            answer[n - 1] = int(sss[i])
            n = 0
    answer.reverse()

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))