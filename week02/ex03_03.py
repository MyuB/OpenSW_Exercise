for i in range(0, 2):
    p1 = input("player1 = ")
    p2 = input("player2 = ")

    if (p1 == "가위"):
        if (p2 == "가위"):
            print("draw")
        elif (p2 == "바위"):
            print("player2")
        else:
            print("player1")
    elif (p1 == "바위"):
        if (p2 == "바위"):
            print("draw")
        elif (p2 == "보"):
            print("player2")
        else:
            print("player")
    elif (p1 == "보"):
        if (p2 == "보"):
            print("drwa")
        elif (p2 == "가위"):
            print("player2")
        else:
            print("player1")
    else:
        print("wrong input!")

'''
이렇게 간단한 경우에는 콜론 후에 바로 이어 붙이는 것도 가능하다
'''