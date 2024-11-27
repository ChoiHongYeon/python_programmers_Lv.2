# [1차] 뉴스 클러스터링 (https://school.programmers.co.kr/learn/courses/30/lessons/17677?language=python3)
import re

def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    p = re.compile("[a-z]{2}")
    for i in range(len(str1) - 1):
        if p.match(str1[i : i + 2]):
            str1_list.append(str1[i : i + 2])
    for i in range(len(str2) - 1):
        if p.match(str2[i : i + 2]):
            str2_list.append(str2[i : i + 2])

    intersection = 0
    union = 0
    while str1_list:
        tmp = str1_list[0]
        count_tmp_1 = str1_list.count(tmp)
        count_tmp_2 = str2_list.count(tmp)
        intersection += min(count_tmp_1, count_tmp_2)
        union += max(count_tmp_1, count_tmp_2)
        while tmp in str1_list:
            str1_list.remove(tmp)
        while tmp in str2_list:
            str2_list.remove(tmp)
    union += len(str2_list)

    if intersection == 0 and union == 0:
        return 65536
    return int(intersection * 65536 / union)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))