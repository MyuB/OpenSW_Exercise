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

'''
괜찮게 풀었지만 문제랑 해답이랑 서로 다름
def Fact(n):
    if n <= 1: 
        return "Error"
    else:
        result = 1
        
    for i in range(2, n+1):
        result *= i
        
    return result

Fact(5)
'''