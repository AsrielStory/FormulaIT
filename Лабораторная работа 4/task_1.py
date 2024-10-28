import json
from itertools import product

FILENAME = 'input.json'


def task() -> float:
    """Сумма произведений score на weight полученные из файла FILENAME"""
    with open(FILENAME, 'r', encoding="UTF-8") as file:
        json_data = json.load(file)

    score_x_weight = [item["score"] * item["weight"] for item in json_data]
    sum_result = sum(score_x_weight)

    return round(sum_result, 3)


print(task())
