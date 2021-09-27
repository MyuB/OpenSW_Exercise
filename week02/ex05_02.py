def input_num():
    while(1):
        temp = input("2자리 자연수를 입력하세요")
        if len(temp) < 2 or len(temp) > 2:
            print("2자리 자연수가 아닙니다. 다시 입력하세요")
        elif len(temp) == 2:
            break

    return temp


def mul(num1, num2):
    print("%4s" % num1)
    print("X%3s" % num2)
    print("-----")
    print("%4s" % (int(num1) * int(num2[1])))
    print("%3s" % (int(num1) * int(num2[0])))
    print("-----")
    print("%4s" % (int(num1) * int(num2)))

print("1. 1번째 2자리 자연수 출력")
num1 = input_num()
print("2. 2번째 2자리 자연수 출력")
num2 = input_num()
print("3. 곱셈 결과 출력")
mul(num1, num2)


'''
% 스타일 print는 잘 못하겠다

def input_num():
    
    while True:
        num = input("2자리 자연수를 입력하세요: ")
        
        if int(num) >= 10 and int(num) < 100:
            break
        else:
            print("2자리 자연수가 아닙니다. 다시 입력하세요.")
    
    return num

def mul(numA, numB):
       
    print("%4s" % numA)
    print("X%3s" % numB)
    print("----")
    print("%4s" % (int(numA)*int(numB[1])) )
    print("%3s " % (int(numA)*int(numB[0])) )
    print("----")
    print("%4s" % (int(numA)*int(numB)) ) 

print("1. 1번째 2자리 자연수 출력")
numA = input_num()

print("2. 2번째 2자리 자연수 출력")
numB = input_num()

print("3. 곱셈 결과 출력")
mul(numA, numB)
'''