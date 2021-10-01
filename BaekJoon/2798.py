#brute force / 블랙잭(브2)
'''
'가능한 모든 경우의 수를 탐색'
'''

n, m = map(int, input().split())

card = list(map(int, input().split()))
card_len = len(card)
result = 0

for i in range(0, card_len-2):      #카드1개선택
    for j in range(i+1, card_len-1):        #카드1개선택
        for k in range(j+1, card_len):      #카드1개 선택
            if card[i] +card[j] +card[k] > m:       #총 카드3개
                continue
            else:
                result = max(result, card[i] +card[j] +card[k])
print(result)