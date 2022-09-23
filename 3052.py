# 나머지

remainder_count = set()
for i in range(10):
    num = int(input())
    remainder = num % 42
    remainder_count.add(remainder)
print(len(remainder_count))