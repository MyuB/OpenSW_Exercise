d = input("dic = ")
d = d.lstrip("{").rstrip("}").split(",")
out_dict = {}
temp_list = []
for i in range(0, len(d)):
    d[i] = d[i].strip().split(":")
    for k in d[i]:
        k = k.strip("\"").strip().lstrip("\'").rstrip("\'").strip()
        temp_list.append(k)

for i in range(0, len(temp_list), 2):
    out_dict[temp_list[i]] = temp_list[i+1]
print(out_dict)
print(out_dict.keys())
print(out_dict.values())

#마찬가지로 내가 너무 어렵게 INPUT을 받을 것 같다
'''
dic = { 'Kim' : 'Math', 'Lee' : 'English','Han' : 'Art', 'Ahn' : 'Physics'}
print('dic = ',dic)

del dic['Lee']
print(dic.keys())
print(dic.values())
'''
