#brute force / 블랙잭(브2)
'''
m
'''

n, m = map(int, input().split())

card = list(map(int, input().split()))
card = sorted(card, reverse=True)
card_len = len(card)
result = 0

for i in range(0, card_len-2):
    for j in range(i+1, card_len-1):
        for k in range(j+1, card_len):
            if card[i] +card[j] +card[k] > m:
                continue
            else:
                result = max(result, card[i] +card[j] +card[k])
print(result)