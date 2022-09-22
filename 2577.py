# 숫자의 개수 

# 모듈 사용 x
total_num = 1
num_count_dict = {}
for i in range(3):
    total_num *= int(input())

for num in str(total_num):
    if num_count_dict.get(num) is None:
        num_count_dict[num] = 1
    else:
        num_count_dict[num] += 1

for i in range(10):
    if num_count_dict.get(str(i)) is None:
        print(0)
    else:
        print(num_count_dict.get(str(i)))


# 모듈 사용 
from collections import Counter

a, b, c = int(input()), int(input()), int(input())
num_count = Counter(str(a * b * c))
for num in range(10):
    if num_count.get(str(num)) is None:
        print(0)
    else:
        num_count.get(str(num))
