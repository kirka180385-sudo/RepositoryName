salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
increased_spend = spend
for i in range(1, months+1):
    remains = salary - increased_spend
    increased_spend = increased_spend * (increase + 1)
    money_capital += remains
money_capital = abs(int(money_capital))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
