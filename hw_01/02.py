class Menu:
    def __init__(self):
        total = 0
        orderList = {}
        temp_list = []
        f = open('cafe.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            temp_list.append(line.rstrip().split(','))
        f.close()
        for value in temp_list:
            orderList['num'] = value[0]
            orderList['name'] = value[1]
            orderList['금액'] = value[2] + '원'
            orderList['재고'] = value[3]

    def addMenu(self, f):
        print('add menu')
        #cafe.txt를 입력받아 orderList에
        # 주어진 값을 추가하는 함수

    def printMenu(self):
        print('=' * 30)

        print('=' * 30)

class Order(Menu):
    def __init__(self):
        Menu()
        orderResult = []


    def orderMenu(self, menuNum):

        Menu.printMenu()


Menu()