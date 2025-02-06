#近い素数を見つけ素因数分解
from sympy import isprime

n = int(input())

def prime(x):
    i = 2
    while True:
        if x % i == 0:print(i);x /= i
        else:i += 1
        if i > x:break
        

for i in range(10000):
    if isprime(n+i):
        print(n+i);break
    if i < n:      
        if isprime(n-i):
            print(n-i);break
        
prime(n)

