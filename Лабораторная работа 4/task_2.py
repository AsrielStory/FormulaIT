import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Перевод CSV -> JSON из файла INPUT_FILENAME в OUTPUT_FILENAME"""
    data = []
    with open(INPUT_FILENAME, 'r', encoding='UTF-8') as file:
        input_data = csv.DictReader(file, delimiter=',', lineterminator='\n')
        for item in input_data:
            data.append(item)

    with open(OUTPUT_FILENAME, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
