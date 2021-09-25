name1 = input("A = ")
name2 = input("B = ")
ph1 = input("numberA = ")
ph2 = input("numberB = ")

print(f"{name1} {ph1} --> ", end="")
name1[0].upper()
ph1 = ph1.split("-")
#ph1.replace('-', '') 이 코드도 사용할 수 있다
print(f"{name1} {ph1[0]+ph1[1]+ph1[2]}")

print(f"{name2} {ph2} --> ", end="")
name2[0].upper()
ph2 = ph2.split("-")
#ph2.replace('-', '') 이 코드도 사용할 수 있다
print(f"{name2} {ph2[0]+ph2[1]+ph2[2]}")

'''
A = 'abel'
B = 'nenny'
numberA = "010-1234-5678"
numberB = "010-9876-5432"

upperA = A[0].upper() + A[1:]
print(A, numberA, "-->", upperA, numberA.replace('-', ''))

upperB = B[0].upper() + A[1:]
print(B, numberB, "-->", upperB, numberB.replace('-', ''))
'''