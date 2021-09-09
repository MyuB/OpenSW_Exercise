x = int(input("please input x: "))
y = int(input("please input y: "))

print(f'x: {x}')
print(f'y: {y}')
print(f'add: {x + y} sub: {x - y} mul: {x * y} div: {x /y}')

x = int(input("please input x: "))
y = int(input("please input y: "))

print(f'x: {x}')
print(f'y: {y}')
print(f'{x} X {y} = {x * y}')

num = int(input("Please enter the number: "))
for i in range(num, 0, -1):
    for k in range(0, i):
        print("*", end="")
    print()

sum = 0
for i in range(1, 11):
    sum += i
    print(f'{i} --> {sum}')
sum = 0
num = 1
while(num <= 10):
    sum += num
    print(f'{num} --> {sum}')
    num += 1
