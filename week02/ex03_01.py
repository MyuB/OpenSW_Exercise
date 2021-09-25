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

#아니 이거도 내가 너무 어렵게 푼거 같음
#그냥 간단하게 풀면 되는데 너무 2^4의 CASE를 생각해야 한다라고 생각한듯
'''
a = (5, 5)
b = (5, -5)

if a == b:
    print("The same points")
elif a[0] == -b[0] and a[1] == b[1]:
    print("X-axis symmetry")
elif a[0] == b[0] and a[1] == -b[1]:
    print("Y-axis symmetry")
elif a[0] == -b[0] and a[1] == -b[1]:
    print("Origin symmetry")
else:
    print("Nothing")
'''