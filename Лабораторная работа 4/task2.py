# TODO импортировать необходимые модули
import csv
import json
from typing import List, Dict, Any

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файлa
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        # Читаем CSV файл с разделителем ","
        csv_reader = csv.DictReader(csv_file)

        # Преобразуем в список словарей
        data: List[Dict[str, Any]] = list(csv_reader)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")






