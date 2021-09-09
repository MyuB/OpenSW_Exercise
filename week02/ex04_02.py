l = input("insert list of integers with comma")
l = l.lstrip('[').rstrip(']').split(',')
sum = 0
temp = 0
for i in range(0, len(l)):
    l[i] = int(l[i])
    sum += l[i]
    temp += l[i] ** 2

mean = sum / len(l)
var = temp / len(l) - mean ** 2
print(f"Means: {mean}")
print(f"Variance: {var}")

