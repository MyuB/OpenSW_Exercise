for i in range(2):
    prime = []
    comps = []
    a = input("a = ")
    a = a.lstrip('[').rstrip(']').split(',')
    for k in a:
        k = int(k)
        isPrime = True
        for j in range(2, k):
            if k % j == 0:
                isPrime = False
                break

        if isPrime:
            prime.append(k)
        else:
            comps.append(k)

    print(f"Prime_Numbers: {prime} {len(prime)}")
    print(f"Composite_Numbers: {comps} {len(comps)}")

'''
input부분만 제외하면 깔끔하게 짠듯
a = [2, 4, 6, 8, 10, 12, 16, 37, 74]
b = 0
prime_num = []
prime_num_cnt = 0
composite_num = []
composite_num_cnt = 0

for i in a:
    for j in range (2, i):
        if i % j == 0:
            b = 1
            
    if b == 0:
        prime_num.append(i)
        prime_num_cnt+=1
        
    else:
        composite_num.append(i)
        composite_num_cnt += 1
        
    b = 0
        
print("Prime numbers: ", prime_num, prime_num_cnt)
print("Composite_numbers: ", composite_num, composite_num_cnt)

'''