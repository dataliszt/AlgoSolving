# 소수 찾기 


## 틀린정답 
import sys 
count = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().split()))
prime_list = [2, 3, 5, 7] 

curr_count = 0
for num in find_list:
    if num == 1:
        continue 
    elif num in prime_list:
        curr_count += 1
    else:
        cnt = False
        for prime_num in prime_list:
            if num % prime_num == 0:
                cnt = True
                break 
        if not cnt:
            curr_count += 1
            prime_list.append(num)
print(curr_count)


## 맞춘 정답 

import sys 
count = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().rstrip().split()))
def prime_num_count(n_list):
    curr_count = 0
    for num in n_list:
        if num == 1:
            continue 

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            curr_count += 1
    print(curr_count)
    
prime_num_count(find_list)
    

