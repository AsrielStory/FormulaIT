salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Финансовая подушка

for _ in range(months):
    money_capital += spend - salary  # Необходимая подушка на месяц
    spend *= 1 + increase  # Рост цен

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
