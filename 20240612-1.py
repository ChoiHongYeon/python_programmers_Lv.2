# 호텔 대실 (https://school.programmers.co.kr/learn/courses/30/lessons/155651)

def solution(book_time):
    
    for i in book_time:
        i[0] = int(i[0][:2]) * 60 + int(i[0][3:])
        i[1] = int(i[1][:2]) * 60 + int(i[1][3:])
        i[1] += 10
    book_time.sort()

    answer = 0
    ending = []
    for i in range(len(book_time)):
        if ending == []:
            ending.append(book_time[i][1])
            if len(ending) > answer:
                answer = len(ending)
        else:
            ending.sort()
            if book_time[i][0] >= ending[0]:
                del(ending[0])
                ending.append(book_time[i][1])
            else:
                ending.append(book_time[i][1])
            if len(ending) > answer:
                    answer = len(ending)

    return answer

result1 = solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
result2 = solution([["09:10", "10:10"], ["10:20", "12:20"]])
result3 = solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])

print(result1, result2, result3)