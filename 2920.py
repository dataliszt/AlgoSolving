
# 음계 

play_order = ''.join(input().split())
if play_order == "12345678":
    print("ascending")
elif play_order == "87654321":
    print("descending")
else:
    print("mixed")