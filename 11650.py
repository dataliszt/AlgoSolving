# 좌표 정렬하기 

import sys 
n = int(sys.stdin.readline().rstrip())
string_list = []
for i in range(n):
    string_list.append(sys.stdin.readline().rstrip())

string_list = sorted(string_list, key=lambda x : (int(x.split(" ")[0]), int(x.split(" ")[1])))
for string in string_list:
    print(string)