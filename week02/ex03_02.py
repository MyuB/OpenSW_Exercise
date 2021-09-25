for i in range(1, 6):
    t = input(f"case {i}. time = ")
    t = t.split(':')

    for k in range(0, 2):
        t[k] = int(t[k])
    #분이 30보다 적어서 바꿔야 할 경우
    if t[1] - 30 < 0:
        #00시가 들어왔을 경우
        if (t[0] - 1 < 0):
            t[0] = '23'
        #00시 이상인 경우
        else:
            if t[0] < 10:
                t[0] = '0' + str(t[0] - 1)
            else:
                t[0] = str(t[0] - 1)
                
        #분 작업
        t[1] = t[1] + 30
        if (t[1] < 10):
            t[1] = '0' + str(t[1])
    # 앞에 시간은 안바꿔도 되는 경우(분이 30이상인 경우)
    else:
        if (t[0] < 10):
            t[0] = '0' + str(t[0])
        #분 작업
        t[1] = t[1] - 30
        if (t[1] < 10):
            t[1] = '0' + str(t[1])


    out = str(t[0]) + ":" + str(t[1])
    print(out)

#너무 어렵게 생각했다 형변환을 너무 어렵게 진행했다.

'''
t = "10:20"
h = int(t[:2])
m = int(t[3:])

if m > 30:
    if (h < 10):
        print("0" + str(h) + ":" + str(m - 30))
    else:
        print(str(h) + ":" + str(m - 30))
    
elif m < 30:
    if h > 0:
        if (h < 11):
            print("0" + str(h - 1) + ":" + str(m + 30))
        else:
            print(str(h - 1) + ":" + str(m + 30))
    else:
        print("23:" + str(m + 30))
'''