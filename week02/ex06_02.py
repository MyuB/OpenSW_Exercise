import statistics

def student(name, s1, s2, s3):
    scores = [s1, s2, s3]
    mean = round(statistics.mean(scores), 2)
    grade = ''
    if mean > 90:
        grade = 'A'
    elif mean > 80:
        grade = 'B'
    else:
        grade = 'C'

    f = open('student.txt', 'a')
    f.write(f"{name}|{s1}|{s2}|{s3}|{mean}|{grade}\n")
    f.close()

student('Jerry', 90, 89, 99)
student('Eric', 56, 45, 80)
student('Sun', 20, 79, 60)
student('Jacob', 40, 39, 98)