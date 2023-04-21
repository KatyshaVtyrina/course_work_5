from classes.hh import HH


def test_get_request_hh(hh):
    """Ожидается ответ на запрос в формате dict или обработка исключения"""
    assert type(hh.get_request()) is dict

    HH.URL = ''
    assert hh.get_request() == print('Не удается получить данные')

    HH.URL = 'https://api.hh.ru/vacancies'


def test_get_info(vacancies_from_json):
    """Ожидается получение информации о вакансии в нужном формате"""

    assert HH.get_info(vacancies_from_json[0]) == (1, 'Бортпроводник', 1373, 'Москва',
                                                   None, 'https://hh.ru/vacancy/79324625')
    assert HH.get_info(vacancies_from_json[1]) == (2, 'Инженер', 1373, 'Казань', 1000, 'https://hh.ru/vacancy/79324625')
    assert HH.get_info(vacancies_from_json[2]) == (3, 'Специалист по продажам', 1373, 'Санкт-Петербург',
                                                   None, 'https://hh.ru/vacancy/79324625')
    assert HH.get_info(vacancies_from_json[3]) == (4, 'Регистратор', 1373, 'Санкт-Петербург',
                                                   None, 'https://hh.ru/vacancy/79324625')


def test_get_vacancy_hh(hh):
    """Ожидается получение списка вакансий"""
    assert isinstance(hh.get_vacancies(), list)
