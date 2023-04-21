import json


def read_json(file) -> list:
    """Читает json-файл"""
    with open(file) as f:
        data = json.load(f)
    return data


def get_employers(data: list) -> list:
    """Получает список кортежей из списка словарей"""
    employers = []
    for item in data:
        employers.append((item['id'], item['title']))
    return employers


def print_info(choice: str, data: list):
    """Печатает информацию в зависимости от выбора пользователя"""
    if choice == '3':
        salary = ''
        for item in str(data):
            if item.isdigit():
                salary += item
        return salary

    else:
        count = 1
        for item in data:

            if choice == '1':
                print(f'{count}. {item[0]} - {item[1]} вакансий')
            elif choice == '2':
                print(f'{count}. {item[1]} - {item[0]}({item[3]}), зарплата - {item[2]}')
            elif choice == '4':
                print(f'{count}. {item[0]} - {item[1]} рублей')
            elif choice == '5':
                print(f'{count}. {item[0]}')

            count += 1
