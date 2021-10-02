print("1번째 n자리 정수 출력")
while(True):
    x = input("n자리의 정수를 입력하세요: ")
    try:
        int(x)
        break
    except ValueError:
        continue
print("2번째 n자리 정수 출력")
while(True):
    y = input("n자리의 정수를 입력하세요: ")
    try:
        int(y)
        break
    except ValueError:
        continue

final_answer = int(x) * int(y)
# 출력되는 최대 자리수를 맞춰주기 위해 지정한 변수
# 문자열 포맷팅을 사용하려고 했지만, 포매팅으로 정렬할 때는 숫자밖에 사용하지 못하는 것 같다.
total_length = len(str(final_answer))
print(f"{x:>{total_length}s}")
print("x" + f"{y:>{total_length - 1}s}")
print('-' * total_length)
#세부 구현

#중간에 있는 것들을 담아놓는 리스트
calced_list = []

#음수 판별
if (x[0] == '-'):
    x = x[1:]
if (y[0] == '-'):
    y = y[1:]

temp = y
for i in range(0, len(y)):
    divisor = pow(10, len(temp) - 1)
    calced_list.append(int(x) * (int(temp) // divisor))
    temp = temp[1:]

calced_list.reverse()
count = 0
for e in calced_list:
    print(f"{str(e) + ' ' * count:>{total_length}s}")
    count += 1

print('-' * total_length)
print(final_answer)
