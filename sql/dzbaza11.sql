-- Подключиться к базе данных hr
use hr;
--  Вывести список region_id, total_countries, 
-- где total_countries - количество стран в таблице. 
-- Подсказка: работаем с таблицей countries, использовать 
-- оконную функцию over() и суммировать count(country_id).--
SELECT
    region_id,
    COUNT(country_id) OVER () AS total_countries
FROM
    countries;
-- Изменить запрос 2 таким образом, чтобы для каждого region_id выводилось количество стран в этом регионе. Подсказка: добавить partition by region_id в over()
SELECT
    region_id,
    COUNT(country_id) OVER (PARTITION BY region_id) AS total_countries
FROM
    countries;
-- Работа с таблицей departments. Написать запрос, который выводит location_id, department_name, dept_total, где dept_total - количество департаментов в location_id.
SELECT 
	location_id, department_name,
	COUNT(department_name) OVER (PARTITION BY location_id) as dept_total
    from departments;
-- Изменить запрос 3 таким образом, чтобы выводились названия городов соответствующих location_id. 
SELECT
DISTINCT
 c.region_id,
 l.city,
 COUNT(c.country_id) OVER (PARTITION BY c.region_id) AS total_countries
FROM countries c
 JOIN locations l
 ON c.country_id = l.country_id;
-- Работа с таблицей employees. Вывести manager_id, last_name, total_manager_salary, где total_manager_salary - общая зарплата подчиненных каждого менеджера (manager_id). 
SELECT
    e.manager_id,
    e.last_name,
    mgr_salaries.total_manager_salary
FROM
    employees e
JOIN (
    SELECT
        manager_id,
        SUM(salary) AS total_manager_salary
    FROM
        employees
    GROUP BY
        manager_id
) mgr_salaries
ON e.employee_id = mgr_salaries.manager_id
ORDER BY
    e.manager_id, e.last_name;
