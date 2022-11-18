# 요세푸스 문제 0 

import sys 
n, k = map(int, sys.stdin.readline().split())
y_list = [x for x in range(1, n + 1)]
temp_list = []
cnt = 0 
while True:
    if len(y_list) == 0:
        break 
    for num in y_list:
        cnt += 1
        if cnt == k:
            temp_list.append(num)
            cnt = 0
    y_list = [x for x in y_list if x not in temp_list]
print(f'<{", ".join(list(map(str, temp_list)))}>')

        