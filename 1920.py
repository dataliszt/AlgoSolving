# 수 찾기 

import sys 
n = int(sys.stdin.readline().rstrip())
search_list = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
check_list = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(search_list, target):
    start = 0
    end = len(search_list) - 1
    while start <= end:
        center = (start + end) // 2
        if search_list[center] == target:
            return 1
        elif search_list[center] > target:
            end = center - 1
        else:
            start = center + 1
    return 0

search_list.sort()
for target in check_list:
    print(binary_search(search_list, target))
    
    
