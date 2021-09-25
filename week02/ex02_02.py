list1 = []
list2 = []
for i in range(1, 11):
    if i % 2 == 0:
        list2.append(i)
    else:
        list1.append(i)

result = list1 + list2
result.sort(reverse=True)
#print(f"{list1}")
#print(f"{list2}") 이거 출력 안했었음
print(result)

'''
odd=(list(range(1,11,2)))
even=(list(range(2,11,2)))
print("list1:",odd)
print("list2:",even)

result = odd + even
result.sort(reverse = True)
print("result:",result)
'''