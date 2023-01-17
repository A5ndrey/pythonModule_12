counter_sum_ticket = 0
ticket = int(input("Введите количество билетов:\t"))
for i in range(ticket, 0, -1):
    age = int(input("Укажите возраст:\t"))
    if age < 18:
        cost = 0
    elif 18 <= age < 25:
        cost = 990
    elif age > 25:
        cost = 1390
    counter_sum_ticket += cost
if ticket > 3:
    counter_sum_ticket = counter_sum_ticket - (counter_sum_ticket + cost) * 10 / 100
print(int(counter_sum_ticket), "руб.")
