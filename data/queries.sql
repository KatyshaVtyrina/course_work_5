--создание базы данных
CREATE DATABASE head_hunter;

--создание таблиц
CREATE TABLE IF NOT EXISTS employers
(
	employer_id int PRIMARY KEY,
	employer_name varchar(255) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS vacancies
(
	vacancy_id int PRIMARY KEY,
	vacancy_name varchar(255) NOT NULL,
	employer_id int REFERENCES employers(employer_id) NOT NULL,
	city varchar(255),
	url text,
	salary int
);

--companies_and_vacancies_count
SELECT employer_name, COUNT(*) as quantity_vacancies
FROM vacancies
LEFT JOIN employers USING(employer_id)
GROUP BY employer_name
ORDER BY quantity_vacancies DESC, employer_name

--all_vacancies
SELECT employers.employer_name, vacancy_name, salary, url
FROM vacancies
JOIN employers USING(employer_id)
WHERE salary IS NOT NULL
ORDER BY salary DESC, vacancy_name

--avg_salary
SELECT ROUND(AVG(salary)) as average_salary
FROM vacancies

--vacancies_with_higher_salary
SELECT vacancy_name, salary
FROM vacancies
WHERE salary > (SELECT AVG(salary) FROM vacancies)
ORDER BY salary DESC, vacancy_name

--
SELECT vacancy_name
FROM vacancies
WHERE vacancy_name ILIKE '%python%'
ORDER BY vacancy_name
