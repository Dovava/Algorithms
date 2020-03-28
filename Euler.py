import sympy
x = 600851475143
for i in range(2,x+1):
                if sympy.isprime(i) and x % i == 0:
                                print(i)
