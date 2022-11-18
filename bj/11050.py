# 이항 계수 1

import sys 

n, k = map(int, sys.stdin.readline().split())

# 브루트포스 
n_fac = 1
k_fac = 1
nk_fac = 1
for i in range(n, 0, -1):
    n_fac *= i
    if i <= k:
        k_fac *= i 
    if i <= n - k:
        nk_fac *= i
print(int(n_fac / (k_fac * nk_fac)))


# 재귀 
def factorial(n):
    if n <= 1:
        return 1 
    return n * factorial(n - 1)
print(int(factorial(n) / (factorial(k) * factorial(n-k))))