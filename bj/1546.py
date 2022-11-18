# 평균 

subject_cnt = int(input())
score_list = list(map(int, input().split()))
max_value = max(score_list)
total_score = 0
for idx, score in enumerate(score_list):
    if score == 0:
        continue
    total_score += score / max_value * 100 
print(total_score / subject_cnt)