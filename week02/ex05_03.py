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

'''
import math

def student_grade(num):
    d = []
    i = 0
    
    while i < int(num):
        value = input("학생%d의 점수를 입력하세요: " %i)
        
        if int(value) < 0 or int(value) > 100:
            continue
        else:
            d.append(int(value))
            i+=1  
               
    return d
            
def grade_calculator(grade):
    sum, avg, std = 0, 0, 0
    sortedGrade = sorted(grade)
    
    for value in grade:
        sum += value
    
    avg = sum / len(grade)
    
    for value in grade:
        std += (value - avg)**2
    
    std = math.sqrt(std/len(grade))
    
    maxGrade = sortedGrade[-1]
    minGrade = sortedGrade[0]
    
    print("학생 점수:", grade)
    print("평균:", avg)
    print("표준편차:", std)
    print("최고점:", "학생" + str(grade.index(maxGrade)), maxGrade)
    print("최저점:", "학생" + str(grade.index(minGrade)), minGrade)
        
while True:
    studentNum = input("학생 수를 입력하세요: ")
    if int(studentNum) > 0 and int(studentNum) <= 10:
        break
    else:
        print("학생 수는 1명이상 10명이하여야 합니다.")
        
studentGrade = student_grade(studentNum)
grade_calculator(studentGrade)
'''