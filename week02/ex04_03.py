l = input("insert list of scores")
l = l.lstrip('[').rstrip(']').split(',')
for i in range(0, len(l)):
    l[i] = int(l[i])
    if (l[i] >= 90):
        print(f"{i}번 학생은 {l[i]}점으로 A학점입니다.")
    elif (l[i] >= 80):
        print(f"{i}번 학생은 {l[i]}점으로 B학점입니다.")
    elif (l[i] >= 70):
        print(f"{i}번 학생은 {l[i]}점으로 C학점입니다.")
    elif (l[i] >= 60):
        print(f"{i}번 학생은 {l[i]}점으로 D학점입니다.")
    else:
        print(f"{i}번 학생은 {l[i]}점으로 F학점입니다.")

'''
코드가 깔끔하지 않다. 그냥 grade 자체를 비교했으면 되었을텐데

result = [55,90,89,76,37,100,67]

for i in range(len(result)):
    if result[i] >= 90:
        grade = "A"
        
    elif result[i] >= 80:
        grade = "B"
        
    elif result[i] >= 70:
        grade = "C"
        
    elif result[i] >= 60:
        grade = "D"   
        
    else:
        grade = "F"
        
    print("%d번 학생은 %d점으로 %s입니다." % (i+1, result[i], grade))

'''