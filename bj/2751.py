
# 수 정렬하기 2


### 맞춘풀이
import sys 
n = int(sys.stdin.readline().rstrip())
tmp_list = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    tmp_list.append(num)
tmp_list.sort()
for num in tmp_list:
    print(num)
        
        

## 오답 

import sys 
n = int(sys.stdin.readline().rstrip())
unsorted_list = []
for i in range(n):
    unsorted_list.append(int(sys.stdin.readline().rstrip()))

for i in range(len(unsorted_list) - 1):
    for j in range(len(unsorted_list) - i - 1):
        if unsorted_list[j] > unsorted_list[j + 1]:
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
for i in unsorted_list:
    print(i)


import sys 
n = int(sys.stdin.readline().rstrip())
max_value = 0 
min_value = 0
tmp_dict = {}
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    tmp_dict[num] = 1
    max_value = max(0, num)
    min_value = min(0, num)

for j in range(min_value, max_value + 1):
    if j in tmp_dict.keys():
        print(j)