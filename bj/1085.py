# 직사각형에서 탈출 

x, y, w, z = map(int, input().split())

x_distance = min(abs(x - 0), w - x) 
y_distance = min(abs(y - 0), z - y)

print(min(x_distance, y_distance))