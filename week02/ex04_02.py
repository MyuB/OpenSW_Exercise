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

'''
scores = [100, 90, 80, 55, 95, 80, 65, 75, 70, 90]
sum = 0
for i in scores:
    sum = sum + i

mean = sum/len(scores)

vsum = 0
for i in scores:
    vsum = vsum + (i - mean)**2
    
variance = vsum / len(scores)

print("Means :", mean)
print("Variance :", variance)
'''