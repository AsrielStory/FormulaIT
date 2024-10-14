money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

minus = spend - salary  # Ежемесячный минус
month_count = 0  # Прожитые месяцы без долгов

while money_capital + salary - spend > 0:
    money_capital = money_capital + salary - spend  # Ежемесячное движение капитала
    spend *= 1 + increase  # Рост цен
    month_count += 1  # Добавление прожитого месяца без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month_count)
