# 素因数分解

n = int(input())
i = 2

while True:
    if n % i == 0:print(i);n /= i
    else:i += 1
    if i > n:break