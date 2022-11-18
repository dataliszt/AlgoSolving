# OX 퀴즈 

repeat_time = int(input())
for i in range(repeat_time):
    string = input()
    total_score = 0 
    score = 0
    for char in string:
        if char == "O":
            score += 1
            total_score += score
        else:
            score = 0 
    print(total_score)