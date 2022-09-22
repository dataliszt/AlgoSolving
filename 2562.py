# 최댓값 

num_dict = {}
for i in range(1, 10):
    num_dict[int(input())] = i 
print(max(list(num_dict.keys())))
print(num_dict[max(list(num_dict.keys()))])
    