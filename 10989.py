# 수 정렬하기 3 

import sys

# 버블 정렬 - 시간초과 
n = int(sys.stdin.readline().rstrip())
num_list = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    num_list.append(num)
    
def bubble_sort(num_list):
    swap = 0
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - 1 - i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swap += 1
        if swap == 0:
            return num_list 
    return num_list
    

# 퀵정렬 - 시간초과 

def qsort(num_list):
    if len(num_list) <= 1:
        return num_list
    
    pivot = num_list[0]
    left = [x for x in num_list if x < pivot]
    right = [x for x in num_list if x >= pivot]
    
    return qsort(left) + [pivot] + qsort(right)
        
# dict를 활용한 풀이  - 통과 

n = int(sys.stdin.readline().rstrip())
temp_dict = {}
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if temp_dict.get(num):
        temp_dict[num] += 1
    else:
        temp_dict[num] = 1
        
for key in sorted(temp_dict.keys()):
        for _ in range(temp_dict[key]):
            print(key)
