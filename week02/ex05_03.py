import math
import statistics

def student_grade(n):
    student_score = []
    cnt = 0
    while(cnt < n):
        score = int(input(f"학생{cnt}의 점수를 입력해주세요: "))
        if score > 100:
            continue
        elif score < 0:
            continue
        else:
            student_score.append(score)
            cnt += 1

    return student_score

def grade_calculator(score_list):
    sum = 0
    var = 0
    mean = statistics.mean(score_list)
    for i in score_list:
        var += (i - mean) ** 2

    print(f"평균: {statistics.mean(score_list)}")
    print(f"표준 편차: {statistics.stdev(score_list)}")
    print(f"표준 편차: {math.sqrt((var) / len(score_list))}")
    max_index = score_list.index(max(score_list))
    min_index = score_list.index(min(score_list))
    print(f"최고점: 학생{max_index} {score_list[max_index]}")
    print(f"최저점: 학생{min_index} {score_list[min_index]}")

student_num = int(input("학생 수를 입력해주세요: "))
score_list = student_grade(student_num)
print(f"학생 점수: {score_list}")
grade_calculator(score_list)

