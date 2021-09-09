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