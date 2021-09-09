name1 = input("A = ")
name2 = input("B = ")
ph1 = input("numberA = ")
ph2 = input("numberB = ")

print(f"{name1} {ph1} --> ", end="")
name1[0].upper()
ph1 = ph1.split("-")
print(f"{name1} {ph1[0]+ph1[1]+ph1[2]}")

print(f"{name2} {ph2} --> ", end="")
name2[0].upper()
ph2 = ph2.split("-")
print(f"{name2} {ph2[0]+ph2[1]+ph2[2]}")