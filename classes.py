import psycopg2


class PSQL:

    def __init__(self, host: str, database: str, user: str, password: str, port=5432):
        self.conn = None
        self.host = host
        self.database = database
        self.user = user
        self.port = port
        self.password = password

    def connect(self) -> None:
        try:
            self.conn = psycopg2.connect(host=self.host,
                                         database=self.database,
                                         user=self.user,
                                         password=self.password,
                                         port=self.port)
        except psycopg2.OperationalError:
            print("Не удалось подключиться к базе данных")

    def disconnect(self) -> None:
        if self.conn:
            self.conn.close()


class Connector(PSQL):

    def __init__(self, host: str, database: str, user: str, password: str, port=5432):
        super().__init__(host, database, user, password, port)

    def insert(self):
        pass


class DBManager(PSQL):

    def __init__(self, host: str, database: str, user: str, password: str, port=5432):
        super().__init__(host, database, user, password, port)

    def get_companies_and_vacancies_count(self):

        """Получает список всех компаний и количество вакансий у каждой компании"""
        pass

    def get_all_vacancies(self):
        """ Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        pass

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        pass

    def get_vacancies_with_keyword(self) -> list:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”"""
        pass


Connector('localhost', 'tests', 'postgres', '1379').connect()