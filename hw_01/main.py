class Menu:
    def __init__(self):
        self.orderList = {}
        self.total = 0
        self.temp_list = []

    def addMenu(self, file):
        f = open(file, 'r', encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            self.temp_list.append(line.rstrip().split(','))
        f.close()
        for i in range(0, 5):
            self.orderList[i + 1] = self.temp_list[i][1:]

    def printMenu(self):
        print("=" * 35)
        for i in range(0, 5):
            temp = self.orderList[i + 1]
            print(f"{i + 1}.{temp[0][1:]}  금액:{temp[1]} 재고: {temp[2]}")
        print("end를 입력하시면 주문서로 돌아갑니다.")
        print("=" * 35)

class Order(Menu):
    def __init__(self):
        super().__init__()
        self.orderResult = [0, 0, 0, 0, 0]

    def orderMenu(self, menuNum):
        self.printMenu()
        if menuNum > 5 or menuNum < 0:
            print("존재하지 않는 메뉴입니다.")
            return
        print("선택한 메뉴의 수량을 입력해주세요")
        beverage_amount = int(input("input: "))
        temp_values = self.orderList[menuNum]
        if int(temp_values[2]) == 0:
            print("품절되었습니다. 다른 메뉴를 선택해주세요")
            while menuNum >= 1 or menuNum <= 5 or menuNum == "end":
                menuNum = input("input: ")
                if menuNum == "end":
                    break
                menuNum = int(menuNum)
                if menuNum > 5 or menuNum < 0:
                    print("존재하지 않는 메뉴입니다.")
                self.printMenu()
                print("선택한 메뉴의 수량을 입력해주세요")
                beverage_amount = int(input("input: "))
                self.orderResult[menuNum - 1] += beverage_amount
                current_beverage_value = int(self.orderList[menuNum][-1])
                current_beverage_value -= beverage_amount
                self.orderList[menuNum][2] = current_beverage_value

        elif beverage_amount > int(temp_values[2]):
            while beverage_amount <= int(temp_values[2]):
                print("수량이 부족합니다")
                self.printMenu()
                print("선택한 메뉴의 수량을 입력해주세요")
                # 선택한 메뉴의 수량
                beverage_amount = int(input("input: "))
                self.orderResult[menuNum - 1] += beverage_amount
                current_beverage_value = int(self.orderList[menuNum][-1])
                current_beverage_value -= beverage_amount
                self.orderList[menuNum][2] = current_beverage_value
        else:
            self.orderResult[menuNum - 1] += beverage_amount
            current_beverage_value = int(self.orderList[menuNum][-1])
            current_beverage_value -= beverage_amount
            self.orderList[menuNum][2] = current_beverage_value

        while True:
            if menuNum == "end":
                break
            print("추가로 주문할 메뉴 번호를 입력하세요")
            menuNum = input("input: ")
            if menuNum == "end":
                break
            menuNum = int(menuNum)
            if menuNum > 5 or menuNum < 0:
                print("존재하지 않는 메뉴입니다.")
            self.printMenu()
            print("선택한 메뉴의 수량을 입력해주세요")
            # 선택한 메뉴의 수량
            beverage_amount = int(input("input: "))
            temp_values = self.orderList[menuNum]
            #다시 돌아가는거 처리
            if int(temp_values[2]) == 0:
                print("품절되었습니다. 다른 메뉴를 선택해주세요")
                while menuNum >= 1 or menuNum <= 5 or menuNum == "end":
                    menuNum = input("input: ")
                    if menuNum == "end":
                        break
                    menuNum = int(menuNum)
                    if menuNum > 5 or menuNum < 0:
                        print("존재하지 않는 메뉴입니다.")
                    self.printMenu()
                    print("선택한 메뉴의 수량을 입력해주세요")
                    # 선택한 메뉴의 수량
                    beverage_amount = int(input("input: "))
                    self.orderResult[menuNum - 1] += beverage_amount
                    current_beverage_value = int(self.orderList[menuNum][-1])
                    current_beverage_value -= beverage_amount
                    self.orderList[menuNum][2] = current_beverage_value
            elif beverage_amount > int(temp_values[2]):
                while True:
                    print("수량이 부족합니다")
                    self.printMenu()
                    print("선택한 메뉴의 수량을 입력해주세요")
                    # 선택한 메뉴의 수량
                    beverage_amount = int(input("input: "))
                    if beverage_amount <= int(temp_values[2]):
                        break
                    self.orderResult[menuNum - 1] += beverage_amount
                    current_beverage_value = int(self.orderList[menuNum][-1])
                    current_beverage_value -= beverage_amount
                    self.orderList[menuNum][2] = current_beverage_value
            else:
                self.orderResult[menuNum - 1] += beverage_amount
                current_beverage_value = int(self.orderList[menuNum][-1])
                current_beverage_value -= beverage_amount
                self.orderList[menuNum][2] = current_beverage_value

        self.printMenu()
        current_cost = 0
        for i in range(0, 5):
            temp = self.orderList[i + 1]
            current_cost += int(temp[1]) * self.orderResult[i]
        print("주문내역")
        print(f"총 주문 수량: {sum(self.orderResult)}, 총 주문 금액: {current_cost}")
        self.total += current_cost

class Manage(Order):
    def __init__(self):
        super().__init__()
        self.manage_result = 0

    def management(self, menuNum):
        self.printMenu()
        if menuNum > 5 or menuNum < 0:
            print("존재하지 않는 메뉴입니다.")
            return
        print("선택한 메뉴의 수량을 입력해주세요")
        # 선택한 메뉴의 수량
        beverage_amount = int(input("input: "))
        total_beverage_amount = beverage_amount
        self.manage_result += (beverage_amount * int(self.orderList[menuNum][1]))

        while True:
            print("추가로 주문할 메뉴 번호를 입력하세요")
            menuNum = input("input: ")
            if menuNum == "end":
                break
            menuNum = int(menuNum)
            if menuNum > 5 or menuNum < 0:
                print("존재하지 않는 메뉴입니다.")
            self.printMenu()
            print("선택한 메뉴의 수량을 입력해주세요")
            # 선택한 메뉴의 수량
            beverage_amount = int(input("input: "))
            total_beverage_amount += beverage_amount
            self.manage_result += (beverage_amount * int(self.orderList[menuNum][1]))
            
        #마지막에 print 하는 부분 정리
        print(f"총 주문 수량: {total_beverage_amount} 개, 총 주문 금액: {self.manage_result}원")

    def toSale(self):
        print(self.total)


order = Manage()
order.addMenu("cafe.txt")
while True:
    print('=' * 20)
    print('주문서')
    print('=' * 20)
    print("1. 커피 주문하기")
    print("2. 커피 매출 확인")
    print("3. 커피 입고 하기")
    print("4. 종료하기")
    print('=' * 20, "\n")
    print("원하시는 주문 번호를 입력해주세요")
    select_order = input("input: ")

    if select_order == '4':
        print("종료합니다")
        break

    if select_order == '1':
        #총 주문 수량
        print("주문할 메뉴 번호를 입력해주세요")
        menu_num = int(input("input: "))
        order.orderMenu(menu_num)
    elif select_order == '2':
        order.toSale()
    elif select_order == '3':
        print("주문할 메뉴 번호를 입력해주세요")
        menu_num = int(input("input: "))
        order.management(menu_num)
    else:
        print("잘못된 입력입니다!!!!")
