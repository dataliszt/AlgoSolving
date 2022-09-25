# 블랙잭 


n, m  = map(int, input().split())
card_list = sorted(list(map(int, input().split())))
candidate_list = []
for i in range(len(card_list)):
    for j in range(i+1, len(card_list)):
        for k in range(i+2, len(card_list)):
            sum = card_list[i] + card_list[j] + card_list[k]
            if sum <= m:
                candidate_list.append(sum)
print(sorted(candidate_list)[-1])