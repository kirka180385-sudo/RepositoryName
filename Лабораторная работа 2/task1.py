money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
#Первый месяц (без повышения цен)
remains = money_capital + salary
remains  = remains  - spend
count = 1
#Следующие месяца:
increased_spend = spend*(increase+1)
while remains + salary >= increased_spend:
    remains  += salary
    remains  -= increased_spend
    increased_spend = increased_spend*(increase+1)
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
