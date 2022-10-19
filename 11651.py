# 좌표 정렬하기 2

import sys 
n = int(sys.stdin.readline())
string_list = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    string_list.append(temp)
string_list.sort(key=lambda x : (x[1], x[0]))
for item in string_list:
    print(item[0], item[1])
