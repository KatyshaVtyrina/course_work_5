import requests


class HH:
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self, search: int):
        self.search = search
        self.params = {'employer_id': f'{self.search}', 'page': 0, 'per_page': 100}

    def get_request(self):
        """Запрос вакансий через API"""
        try:
            response = requests.get(self.URL, self.params)
            if response.status_code == 200:
                return response.json()

        except requests.RequestException:
            print('Не удается получить данные')

    @staticmethod
    def get_info(data: dict):
        """Получение кортежа в нужном формате"""
        vacancy_id = int(data.get('id'))
        name = data['name']
        employer_id = int(data.get('employer').get('id'))
        city = data.get('area').get('name')
        url = data.get('alternate_url')

        if 'salary' in data.keys():
            if data.get('salary') is not None:
                if 'from' in data.get('salary'):
                    salary = data.get('salary').get('from')
                else:
                    salary = None
            else:
                salary = None
        else:
            salary = None

        vacancy = (vacancy_id, name, employer_id, city, salary, url)
        return vacancy

    def get_vacancies(self) -> list:
        """Получение списка вакансий"""
        vacancies = []
        page = 0
        while True:
            self.params['page'] = page
            data = self.get_request()

            for vacancy in data.get('items'):
                if vacancy.get('salary') is not None and vacancy.get('salary').get('currency') is not None:

                    # если зп рубли, добавляем в список, если нет, пропускаем
                    if vacancy.get('salary').get('currency') == "RUR":
                        vacancies.append(self.get_info(vacancy))
                    else:
                        continue

                # если зп не указана, добавляем в список
                else:
                    vacancies.append(self.get_info(vacancy))

            page += 1

            # если была последняя страница, заканчиваем сбор данных
            if data.get('pages') == page:
                break

        return vacancies
