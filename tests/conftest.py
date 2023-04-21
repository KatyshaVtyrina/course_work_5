import json
import pytest


from classes.hh import HH
from classes.db_manager import DBManager
from utils.config import config


@pytest.fixture
def path():
    return 'tests/test_data/test_vacancies.json'


@pytest.fixture
def hh():
    return HH(1373)


@pytest.fixture
def vacancies_from_json():
    with open('tests/test_data/test_vacancies.json') as file:
        vacancies = json.load(file)
    return vacancies


@pytest.fixture
def db():
    return DBManager('tests', config())


@pytest.fixture
def employers():
    return [(1, 'Тинькофф'), (2, 'VK'), (3, 'Аэрофлот')]


@pytest.fixture
def vacancies():
    vacancies = [(1, 'Разработчик', 1, 'Москва', 10000, 'www'),
                 (2, 'Разработчик - Python', 2, 'Уфа', 20000, 'www'),
                 (3, 'Аналитик', 3, 'Казань', 20000, 'www'),
                 (4, 'Тестировщик', 1, 'Мурманск', 50000, 'www'),
                 (5, 'Python developer', 2, 'Самара', None, 'www')]
    return vacancies
