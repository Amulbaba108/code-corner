n = int(input())
prime = n >= 2 and all(n % i for i in range(2, int(n**0.5) + 1))
print("prime" if prime else "not prime")
