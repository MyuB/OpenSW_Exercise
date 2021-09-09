print("Case 1")
for i in range(0, 2):
    a = input("a = ")
    b = input("b = ")
    a = a.lstrip("(").rstrip(")").split(",")
    b = b.lstrip("(").rstrip(")").split(",")

    for k in range(0, 2):
        a[k] = int(a[k])
        b[k] = int(b[k])

    #x가 같은 경우
    if (a[0] == b[0]):
        #x, y같이 같은 경우
        if (a[1] == b[1]):
            print("same point")
        #y축 대칭인 경우
        elif (a[1] == -b[1]):
            print("y-axis symmetry")
        else:
            print("nothing")
    #x값이 서로 반대인 경우
    elif (a[0] == -b[0]):
        #y같은 같은 경우
        if (a[1] == b[1]):
            print("x-axis symmentry")
        #원점 대칭인 경우
        elif (a[1] == -b[1]):
            print("origin summentry")
        else:
            print("nothing")
    else:
        print("nothing")

