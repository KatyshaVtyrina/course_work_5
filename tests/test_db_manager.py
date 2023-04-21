from decimal import Decimal


def test_create_data_base_and_insert(db):
    """Ожидается создание базы данных и таблиц"""
    db.create_database()


def test_insert(db, employers, vacancies):
    """Ожидается добавление данных в таблицы"""
    db.insert('employers', employers)
    db.insert('vacancies', vacancies)


def test_get_companies_and_vacancies_count(db):
    """Ожидается получение списка всех компаний и количество вакансий у каждой компании"""
    assert db.get_companies_and_vacancies_count() == [('VK', 2), ('Тинькофф', 2), ('Аэрофлот', 1)]


def test_get_all_vacancies(db):
    """Ожидается получение списка всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
    assert db.get_all_vacancies() == [('Тинькофф', 'Тестировщик', 50000, 'www'),
                                      ('Аэрофлот', 'Аналитик', 20000, 'www'),
                                      ('VK', 'Разработчик - Python',  20000, 'www'),
                                      ('Тинькофф', 'Разработчик', 10000, 'www')]


def test_get_avg_salary(db):
    """Ожидается получение средней зарплаты по вакансиям"""
    assert db.get_avg_salary() == [(Decimal('25000'),)]


def test_get_vacancies_with_higher_salary(db):
    """Ожидается получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям"""
    assert db.get_vacancies_with_higher_salary() == [('Тестировщик', 50000)]


def test_get_vacancies_with_keyword(db):
    """Ожидается получение списка всех вакансий, в названии которых содержатся
    переданные в метод слова, например “python”"""
    assert db.get_vacancies_with_keyword('python') == [('Python developer',), ('Разработчик - Python',)]
