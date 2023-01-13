money = int(input())
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

tkb = per_cent['ТКБ'] * money / 100
skb = per_cent['СКБ'] * money / 100
vtb = per_cent['ВТБ'] * money / 100
sber = per_cent['СБЕР'] * money / 100

deposit = [tkb, skb, vtb, sber]

print(list(map(int, deposit)))
print('Максимальная сумма, которую вы можете заработать - ', int(max(deposit)))
