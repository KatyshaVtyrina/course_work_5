from classes.hh import HH
from classes.db_manager import DBManager
from utils.utils import read_json, print_info, get_employers
from utils.config import config

PATH_TO_EMPLOYERS = 'data/employers.json'


def main():
    params = config()
    db = DBManager('head_hunter', params)

    print('Сoздаем базу данных и таблицы')
    print('................................')
    db.create_database()
    print(f'База данных и таблицы созданы')
    print('................................')

    employers = read_json(PATH_TO_EMPLOYERS)
    print('Добавляем данные о работодателях')
    print('................................')
    db.insert('employers', get_employers(employers))
    print('Данные о работодателях добавлены')
    print('................................')

    print('Добавляем данные о вакансиях')
    print('................................')
    for i in range(len(employers)):
        hh = HH(employers[i]['id']).get_vacancies()
        db.insert('vacancies', hh)
    print('Данные о вакансиях добавлены')
    print('................................')

    while True:
        print(f'Меню:\n\
                            1 - вывести список всех компаний и количество вакансий у каждой компании\n\
                            2 - вывести список всех вакансий\n\
                            3 - вывести среднюю зарплату по вакансиям\n\
                            4 - вывести список всех вакансий, у которых зарплата выше средней по всем вакансиям\n\
                            5 - список всех вакансий, в названии которых содержатся переданное в метод слово\n\
                            stop - закончить работу')
        print()
        user_input = input("Введите нужный вариант\n")
        if user_input == '1':
            print('Компании от большего количества вакансий к наименьшему')
            print_info(choice=user_input, data=db.get_companies_and_vacancies_count())

        elif user_input == '2':
            all_vacancies = db.get_all_vacancies()
            print(f'Всего вакансий, где указана зарплата - {len(all_vacancies)}.\n'
                  'Вакансии отсортированы по зарплате от большей к меньшей')
            print_info(choice=user_input, data=all_vacancies)

        elif user_input == '3':
            print(f'Средняя зарплата по всем вакансиям - {print_info(choice=user_input, data=db.get_avg_salary())} '
                  f'рублей')

        elif user_input == '4':
            all_vacancies = db.get_vacancies_with_higher_salary()
            print(f'Всего вакансий, где зарплата выше средней - {len(all_vacancies)}')
            print_info(choice=user_input, data=all_vacancies)

        elif user_input == '5':
            keyword = input('Введите слово, которое будем искать в названии вакансии\n')
            all_vacancies = db.get_vacancies_with_keyword(keyword)
            print(f'Всего вакансий, содержащих "{keyword}" - {len(all_vacancies)}')
            print_info(choice=user_input, data=all_vacancies)

        elif user_input.lower() == 'stop':
            print('Программа завершает работу')
            break

        else:
            print("Такого варианта нет, попробуйте еще раз")
            continue

        print('Показать еще меню? Y/N')
        choice = input().upper()
        if choice == 'Y':
            continue
        else:
            print('Программа завершает работу')
            break

    exit()


if __name__ == '__main__':
    main()
