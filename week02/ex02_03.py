a = input("x = ")
a = tuple(int(x) for x in a.split(","))
b = input("y = ")
b = tuple(str(y) for y in b.split(","))

print(f"x: {a}")
print(f"y: {b}")
print(f"drop {b[-1]}: ", end="")
b = list(b)
del b[-1]
a = list(a)
for y in b:
    a.append(y)
a = tuple(a)
print(a)
