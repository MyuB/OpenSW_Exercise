import math

a = 0
class Square:
    def __init__(self, cx, cy, cr):
        self.cx = cx
        self.cy = cy
        self.cr = cr

    def center(self):
        return (self.cx, self.cy)

    def width(self):
        w = self.cr ** 2
        return w


class Common_area(Square):

    def compute_common_area(self, other):
        x1, y1 = self.cx - self.cr / 2, self.cy + self.cr / 2
        x2, y2 = self.cx + self.cr / 2, self.cy - self.cr / 2
        x3, y3 = other.cx - other.cr / 2, other.cy + other.cr / 2
        x4, y4 = other.cx + other.cr / 2, other.cy - other.cr / 2

        ## case1 other square가 오른쪽으로 벗어나 있는 경우
        if x2 < x3:
            return 0

        ## case2 other square가 왼쪽으로 벗어나 있는 경우
        if x1 > x4:
            return 0

        ## case3 other square가 아래쪽으로 벗어나 있는 경우
        if y2 > y3:
            return 0

        ## case4 other square가 위쪽으로 벗어나 있는 경우
        if y1 < y4:
            return 0

        left_up_x = max(x1, x3)
        left_up_y = min(y1, y3)
        right_down_x = min(x2, x4)
        right_down_y = max(y2, y4)

        width = right_down_x - left_up_x
        height = right_down_y - left_up_y

        return abs(width * height)


print("첫 번째 정사각형의 중심좌표와 한 변의 길이를 입력하세요")
x1 = int(input("x좌표:"))
y1 = int(input("y좌표:"))
r1 = int(input("한 변의 길이:"))
c1 = Common_area(x1, y1, r1)

print("\n두 번째 정사각형의 중심좌표와 한 변의 길이를 입력하세요")
x2 = int(input("x좌표:"))
y2 = int(input("y좌표:"))
r2 = int(input("한 변의 길이:"))
c2 = Common_area(x2, y2, r2)

print("\n첫 번째 정사각형의 좌표, 넓이 :", c1.center(), c1.width())
print("두 번째 정사각형의 좌표, 넓이", c2.center(), c2.width())
print("두 정사각형의 공통 넓이: {0:.2f}".format(c1.compute_common_area(c2)))
if c1.compute_common_area(c2) == 0:
    print("겹치는 부분이 없습니다.")