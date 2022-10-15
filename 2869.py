# 달팽이는 올라가고 싶다 

import sys 

def calc_days(a: int, b: int, v: int) -> int:
    if (v - b) % (a - b): 
        print(int((v - b) //  (a - b)) + 1)
    else:
        print(int((v - b) //  (a - b)))

a, b, v = map(int, sys.stdin.readline().strip().split())
calc_days(a, b, v)