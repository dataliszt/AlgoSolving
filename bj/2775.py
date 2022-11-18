
# 부녀회장이 될테야 

import sys 

# 재귀로 풀면 시간 초과 
def sum_residence(k, n):
    sum = 0
    
    if k == 0:
        return n 
    if k > 0 :
        for i in range(1, n + 1):
            sum += sum_residence(k - 1, i)
    return sum

test_num = int(sys.stdin.readline().strip())
for test in range(test_num):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    print(sum_residence(k, n))
    

# 맞춘 정답

test_num = int(sys.stdin.readline().strip())
for test in range(test_num):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    apartment = []
    for i in range(k):
        floor = []
        for j in range(1, n + 1):
            if i == 0:
                floor.append(j)
            else:
                sum = 0
                for x in apartment[i - 1][:j]:
                    sum += x
                floor.append(sum)
        apartment.append(floor)
    total = 0
    for p in apartment[k - 1]:
        total += p 
    print(total)