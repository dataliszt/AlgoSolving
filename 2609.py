# 최대공약수와 최소공배수 

import sys

num1, num2 = map(int, sys.stdin.readline().strip().split())
tmp1, tmp2 = num1, num2 
while tmp2 > 0:
    tmp1, tmp2 = tmp2, tmp1 % tmp2
print(tmp1, int(num1 * num2 / tmp1), sep="\n")