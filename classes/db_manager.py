import psycopg2
import psycopg2.errors


class DBManager:

    def __init__(self, host: str, database: str, user: str, password: str, port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.port = port
        self.password = password

    def _connect(self) -> None:
        """Подключение к базе данных"""
        try:
            self.conn = psycopg2.connect(host=self.host,
                                         database=self.database,
                                         user=self.user,
                                         password=self.password,
                                         port=self.port)
        except psycopg2.OperationalError:
            print("Не удалось подключиться к базе данных")

    def _disconnect(self) -> None:
        """Отключение от базы данных"""
        if self.conn:
            self.conn.close()

    def insert(self, table: str, data: list) -> None:
        """Добавление данных в базу данных в зависимости от таблицы"""
        try:
            self._connect()
            with self.conn:
                with self.conn.cursor() as cur:
                    if table == 'employers':
                        cur.executemany('INSERT INTO employers(employer_id, employer_name) '
                                        'VALUES(%s, %s)', data)
                    elif table == 'vacancies':
                        cur.executemany('INSERT INTO vacancies(vacancy_id, vacancy_name, employer_name, salary, url) '
                                        'VALUES(%s, %s, %s, %s, %s)', data)

        except psycopg2.errors.UniqueViolation:
            print("Уже есть в таблице")
        finally:
            self._disconnect()

    def _execute_query(self, query) -> list:
        """Возвращает результат запроса"""
        try:
            self._connect()
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute(query)
                    result = cur.fetchall()
        finally:
            self._disconnect()
        return result

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        result = self._execute_query("SELECT employer_name, COUNT(*) "
                                     "FROM vacancies "
                                     "GROUP BY employer_name "
                                     "ORDER BY COUNT(*) DESC")
        return result

    def get_all_vacancies(self):
        """ Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        result = self._execute_query("SELECT employer_name, vacancy_name, salary, url "
                                     "FROM vacancies "
                                     "WHERE salary IS NOT NULL "
                                     "ORDER BY salary DESC")
        return result

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям"""
        result = self._execute_query("SELECT ROUND(AVG(salary)) as average_salary "
                                     "FROM vacancies")
        return result

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        result = self._execute_query("SELECT vacancy_name "
                                     "FROM vacancies "
                                     "WHERE salary > (SELECT AVG(salary) FROM vacancies)")
        return result

    def get_vacancies_with_keyword(self, word) -> list:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”"""
        result = self._execute_query("SELECT vacancy_name "
                                     "FROM vacancies "
                                     f"WHERE vacancy_name LIKE '%{word}%'")
        return result
