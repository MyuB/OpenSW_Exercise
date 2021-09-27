class Shelf:
    def __init__(self):
        self.box = [[], [], [], []]

    def addNum(self, num):

        if self.isFull(num % 4):
            print("%d층은 꽉차서 더이상 공간이 없습니다." % (num % 4 + 1))
        else:
            self.box[num % 4].append(num)

    def delNum(self, num):
        level = -num - 1
        level_size = self.levelSize(-num)

        popObject = None

        if self.isEmpty(level):
            print("%d층은 비어서 제거할 숫자가 없습니다." % (level + 1))
        else:
            popObject = self.box[level][level_size - 1]
            self.box[level] = self.box[level][:level_size - 1]

        return popObject

    def levelSize(self, level):
        if len(self.box[level - 1]) <= 0:
            return 0
        else:
            return len(self.box[level - 1])

    def isFull(self, level):
        is_full = False

        if len(self.box[level]) == 4:
            is_full = True

        return is_full

    def isEmpty(self, level):
        is_empty = False

        if len(self.box[level]) == 0:
            is_empty = True

        return is_empty


S = Shelf()
num = 0
print("-4 <= N <= -1: 각 층의 최근 입력숫자 제거, 나머지 음수: 종료")
while num > -5:
    num = int(input("0혹은 양수 입력: "))

    if num >= -4 and num <= -1:
        S.delNum(num)

    elif num < -4:
        print("종료합니다")
        break

    else:
        S.addNum(num)

    print("--> 현재 box 상태:", S.box)
