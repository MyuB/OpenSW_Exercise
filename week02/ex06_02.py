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


'''
교수님보다 잘짠듯 ㄹㅃㅃ
def student(name,mid,fin,asign):
    avg=(mid+fin+asign) / 3

    if avg>=90:
        score='A'
    elif avg>=80:
        score='B'
    else:
        score='C'

    f=open('students.txt','a')
    data=name+"|"+str(mid)+'|'+str(fin)+'|'+str(asign)+'|'+str(avg)+'|'+score+'\n'
    f.write(data)
    f.close()

student('Jerry',90,89,99)
student('Eric',56,45,80)
student('Sun',20,79,60)
student('Jacob',40,39,98)
'''