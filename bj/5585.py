# 거스름돈

import sys

n = 1000 - int(sys.stdin.readline().strip())

cur_list = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in cur_list:
    cnt += n // coin 
    n %= coin

print(cnt) 