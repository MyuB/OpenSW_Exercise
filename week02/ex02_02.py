list1 = []
list2 = []
for i in range(1, 11):
    if i % 2 == 0:
        list2.append(i)
    else:
        list1.append(i)

result = list1 + list2
result.sort(reverse=True)
print(result)
