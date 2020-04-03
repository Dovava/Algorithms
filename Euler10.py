import sympy
ans,i = (0,1)
while not i > 2000000:
                if sympy.isprime(i):
                                ans += i
                i += 1
                if i % 100000 == 0:
                                print(i)
print(ans)
