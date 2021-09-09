coin = 0
while(1):
    print("1: Insert coin | 2: Item list | 3: Select fruit | 4: Change money | Q: exit")
    a = input("Please select menu: ")

    if a == "2":
        print("::::1. Orange: 300 :::: :::: 2. Shine Muscat : 1000 ::::")
    elif a == "1":
        temp = int(input("How much money do you want to put in?"))
        print(f'You insert {temp} coins')
        coin += temp
    elif a =="3":
        f = input("Which fruit do you want? ")
        if f == "1":
            if coin - 300 < 0:
                print(f"You get {coin} coins back")
            else:
                coin -= 300
                print(f"You get an orange \nYou have {coin} coins")
        elif f == "2":
            if coin - 1000 < 0:
                print(f"You get {coin} coins back")
            else:
                coin -= 1000
                print(f"You get an shine muscat \nYou have {coin} coins")
    elif a == "4":
        print(f"You get {coin} coins back")
        coin = 0
    elif a == "Q":
        print("End")
        break
