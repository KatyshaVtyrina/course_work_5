from utils.utils import read_json, get_employers, print_info


def test_read_json(path):
    """Ожидается распаковка json-файла"""
    assert isinstance(read_json(path), list)


def test_get_employers():
    """Ожидается получение списка кортежей из списка словарей"""
    assert get_employers([{'id': 1, 'title': '1'}, {'id': 2, 'title': '2'}]), [(1, 1), (2, 2)]


def test_print_info(capsys):
    """Ожидается вывод построчно с нумерацией или возврат средней зарплаты"""
    print_info('1', [('Тинькофф', 100), ('VK', 200)])
    captured = capsys.readouterr()
    assert captured.out == "1. Тинькофф - 100 вакансий\n"\
                           "2. VK - 200 вакансий\n"

    print_info('2', [('Тинькофф', 'Разработчик', 100000, 'https://www.tinkoff.ru/'),
                     ('VK', 'Разработчик', 200000, 'https://vk.com/')])
    captured = capsys.readouterr()
    assert captured.out == "1. Разработчик - Тинькофф(https://www.tinkoff.ru/), зарплата - 100000\n" \
                           "2. Разработчик - VK(https://vk.com/), зарплата - 200000\n"

    assert print_info('3', [1000]), 1000

    print_info('4', [('Разработчик', 100000), ('Аналитик', 80000)])
    captured = capsys.readouterr()
    assert captured.out == "1. Разработчик - 100000 рублей\n"\
                           "2. Аналитик - 80000 рублей\n"

    print_info('5', [('Python- разработчик',)])
    captured = capsys.readouterr()
    assert captured.out == "1. Python- разработчик\n"
