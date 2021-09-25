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

'''
조금 더 잘 만들었다면 예외처리를 제대로 했다면 좋았을듯
나쁘게 만들지는 않는 것 같다.

coin = 0
while 1: 
    print("1: Insert coin | 2: Item list | 3: Select fruit | 4: Change money | Q: exit")
    order = input("Please select menu: ")
    
    if order == "1":
        coin = input("\nHow much money do you want to put in? ")
        coin = int(coin)
        try:
            print("You insert", coin, "coins\n")
        except ValueError:
            print("wrong value error! Return to start menu\n")
            
    elif order == "2":
        print("\n::::1. Orange: 300 :::: :::: 2. Shine muscat : 1000::::")
        
    elif order == "3":
        fruit = input("\nWhich fruit do you want?")
        if fruit == "1" and coin >= 300:
            coin = coin - 300
            print("You get an orange\nYou have", coin, "coins\n")
           
        elif fruit == "1" and coin < 300:
            print("You are short of money\nReturn to start menu\n")
            
        elif fruit == "2" and coin >= 1000:
            coin = coin - 1000
            print("You get a shine muscat\nYou have",coin,"coins\n")
            
        elif fruit == "2" and coin < 1000:
            print("You are short of money\nReturn to start menu\n")
        
    elif order == "4":
        print("\nYou get",coin,"coins back\n")
        coin = 0
        
    elif order == "Q":
        break
        
    else:
        continue
        
print("End")
'''