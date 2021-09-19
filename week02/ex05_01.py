def factorial(n):
    sum = 1
    if (n <= 0):
        return "error occured"
    else:
        for i in range(1, n + 1):
            sum *= i
        return sum


for i in range(1, 3):
    n = int(input(f"case{i}: num = "))
    print(factorial(n))