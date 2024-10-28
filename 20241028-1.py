# 영어 끝말잇기 (https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=python3)

def solution(n, words):

    answer = 0

    for i in range(1, len(words)):
        if words[i - 1][len(words[i - 1]) - 1] != words[i][0] or words.index(words[i]) != i or len(words[i]) == 1:
            answer = i
            break

    if answer == 0:
        return [0, 0]
    return [n if (answer + 1) % n == 0 else (answer + 1) % n, int(answer / n) + 1]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))