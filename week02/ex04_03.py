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
