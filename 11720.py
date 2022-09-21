# 숫자의 합

n_count = int(input())
number = input()
total = 0
for i in range(n_count):
    total += int(number[i])
print(total)


#### 다른 풀이 
n_count = int(input())
numbers = list(input())
total = 0
for i in range(n_count):
    total += int(numbers[i])
print(total)