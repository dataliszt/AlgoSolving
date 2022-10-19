# 덩치 
import sys 

n = int(sys.stdin.readline().rstrip())
p_list = []
last = 0 

for _ in range(n):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    p_list.append(info)

for i in range(len(p_list)):
    cnt = 1
    for j in range(len(p_list)):
        if j != i:
            if p_list[i][0] < p_list[j][0] and p_list[i][1] < p_list[j][1]:
                cnt += 1
    p_list[i].append(cnt)
for item in p_list:
    print(item[2])