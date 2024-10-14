numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = 4  # Индекс None элемента

numbers_sum = sum(numbers[:none_index]) + sum(numbers[none_index + 1:])  # Расчёт суммы всех чисел
length = len(numbers)  # Длинна списка
average = numbers_sum / length  # Среднее арифметическое чисел

numbers[none_index] = average  # Замена None элемента на вреднее арифметическое

print("Измененный список:", numbers)
