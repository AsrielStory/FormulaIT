import json
from itertools import product

FILENAME = 'input.json'


def task() -> float:
    """Сумма произведений score на weight полученные из файла FILENAME"""
    with open(FILENAME, 'r', encoding="UTF-8") as file:
        json_data = json.load(file)

    sum_result = sum([item["score"] * item["weight"] for item in json_data])

    return round(sum_result, 3)


print(task())
