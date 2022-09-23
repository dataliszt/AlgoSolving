
# 상수

a, b = map(int, map("".join, map(reversed, input().split())))
print(max(a, b))