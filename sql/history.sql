-- Оконные функции 
use shop;

select
ORDER_ID,
ODATE,
AMT,
sum(AMT) over() as total_amount,
round(AMT / sum(AMT) over(), 3) as percentage_range
from ORDERS;


use shop;
select *
from CUSTOMERS;
select 
	CITY,
    avg(RATING) over (partition by CITY) as average_rating
from CUSTOMERS;

select
ORDER_ID,
AMT,
ODATE,
MAX(AMT) OVER (Partition by extract(Month from ODATE)) as max_sum
from ORDERS;

select 
	*,
    rank() over (order by CUST_ID desc) as rank_id
from ORDERS;

use hr;
select count(*) FROM hr.employees;
-- Вывести сотрудника с самой большой зарплатой.
select max(salary) as max_salary
from hr.employees;
-- Найти количество сотрудников.
select 
сount(last_name)
from hr.employees;
-- Найти сотрудника с самой большой зарплатой.
select employees.first_name, employees.last_name
from hr.employees
where salary = (select max(salary) from hr.employees);
-- Найти среднюю зарплату по компании
select 
avg (salary) as avg_salary
from hr.employees;
-- Найти сотрудников у которых зарплата меньше среднее зарплаты по компании 
select *
from hr.employees 
where salary < (select avg(salary) from hr.employees);
-- Найти количество депортаментов в которых никто не работает
select *
from hr.departments;

select count(*) as sum
from hr.departments as t1
right join hr.employees as t2
on t1.department_id = t2.department_id
where t2.department_id is null;
-- Найти самую большую зарплату в департаменте 70, 80
select max(salary), department_id
From hr.employees
where department_id in (70, 80);
select max(salary)
from hr.employees 
where department_id = 80;

select * 
from country;
select 
SUM(Population) as country_population
From city
group by CountryCode;

select ct.name,
 sum(c.population) as country_population
 from city as c
 inner join country as ct
 on c.CountryCode = ct.Code 
 group by countryCode;
 -- Предоставьте список стран, указав количество используемых языков в каждой из них, выводя отчёт в формате (CountryCode, COUNT(Language)). 
 select * 
 from countrylanguage;
 select
 CountryCode
 count (Language) as count_lng
 from countrylanguage
 group by CountryCode;
 -- Выведите количество сотрудников, работающих в отделах Marketing и IT, используя операцию JOIN между таблицами "employees" и "departments" по полю "department_id"
 select 
 count(employees.employee_id), departments.department_name
 from hr.employees
 join hr.departments on employees.department_id = departments.department_id
 where departments.department_name IN ('Marketing', 'IT')
GROUP BY departments.department_name;
 
 
 -- Вывести текущую дату и время.
select now();
-- Вывести текущий год и месяц
SELECT DATE_FORMAT(NOW(), '%Y, %m');
-- Вывести текущее время
select date_format(now(), '%H, %i');
-- Вывести название текущего дня недели
select case weekday(now())
	WHEN 1 THEN 'Понедельник'
    WHEN 2 THEN 'Вторник'
    WHEN 3 THEN 'Среда'
    WHEN 4 THEN 'Четверг'
    WHEN 5 THEN 'Пятница'
    WHEN 6 THEN 'Суббота'
    WHEN 7 THEN 'Воскресенье'
End as day_of_week;
-- Вывести номер текущего месяца
select month(now());
-- Вывести номер дня в дате “2020-03-18”
select date_format('2023-03-18', '%d');
-- Подключиться к базе данных shop (которая находится на удаленном сервере).
use shop;
-- Определить какие из покупок были совершены апреле (4-й месяц)
SELECT *
FROM ORDERS
WHERE MONTH(odate) = 4;
-- Определить количество покупок в 2022-м году
select * 
from ORDERS 
WHERE year(odate) = 2022;
-- Определить, сколько покупок было совершено в каждый день. Отсортировать строки в порядке возрастания количества покупок. Вывести два поля - дату и количество покупок
SELECT odate AS order_date, COUNT(*) AS order_count
FROM ORDERS
GROUP BY odate
ORDER BY order_count ASC;
-- Определить среднюю стоимость покупок в апреле
SELECT AVG(AMT) AS average_purchase_cost
FROM ORDERS
WHERE MONTH(ODATE) = 4;
-- 1 Подключитесь к базе данных Students (которая находится на удаленном сервере). 
use Students;
-- 2 Найдите самого старшего студента
SELECT first_name, last_name, age as Oldest_Student
FROM Students
WHERE age = (SELECT MAX(age) FROM Students);
-- 3 Найдите самого старшего преподавателя
SELECT name, age as Oldest_Teacher
FROM Teachers
WHERE age = (SELECT MAX(age) FROM Teachers);
-- 4 Выведите список преподавателей с количеством компетенций у каждого
SELECT 
    teacher_id, 
    COUNT(competencies_id) AS competency_count
FROM 
    Teachers2Competencies
GROUP BY 
    teacher_id;
-- 5 Выведите список курсов с количеством студентов в каждом
SELECT 
    student_id, 
    COUNT(course_id) AS course_count
FROM 
    Students2Courses
GROUP BY 
    student_id;
-- 6 Выведите список студентов, с количеством курсов, посещаемых каждым студентом. 
SELECT 
    student_id, 
    COUNT(course_id) AS CoursesCount
FROM 
    Students2Courses
GROUP BY 
    student_id;

use hr;
-- Специальный символы: %d- дни %m- месяц %Y- год
SELECT str_to_date('25,07,2020', '%d, %m, %y');
-- Для вписания времени надо после даты поставить букву Т
select str_to_date('2013-03-17T14:25:39.123', '%Y-%m-%dT%H:%i:%s.%f');
--  Now- текущая дата и время
SELECT DATE_FORMAT(now(), '%Y_%m_%d | %H - %i - %s') as date_now;
-- Сравнение дат DATEDIFF
SELECT datediff('2023-02-01', '2023-01-01');

SELECT TIMESTAMPDIFF(MONTH, '2003-02-01', '2003-05-01');
SELECT TIMESTAMPDIFF(MONTH, '2003-02-18', '2003-05-01');

SELECT TIMESTAMPDIFF(MINUTE,'2003-02-01','2003-05-01 12:05:55');

SELECT TIMESTAMPDIFF(WEEK, '2003-02-18', '2003-05-01');

SELECT * FROM hr.employees
where hire_date between 
'2005-01-01' and
'2005-12-31';

SELECT * FROM hr.employees
where hire_date between 
str_to_date('01-2005-01','%d-%Y-%m') and
str_to_date('31-2005-12','%d-%Y-%m');

use shop;

SELECT avg(AMT) as avg_amount
FROM ORDERS
WHERE date_format(ODATE, '%Y') = 2022;

select NOW() + INTERVAL 1 DAY;
select NOW() - INTERVAL 1 HOUR;





use hr;
select location_id, count(*) as dep_count
from departments
group by location_id
having (location_id between 1400 and 1700) and dep_count > 1;
-- выведите номера отделов и количество сотрудников в каждом отделе, где сотрудников больше 10
select department_id, count(*) as c
from employees group by department_id 
having c > 10;

select department_id, count(*) as c
from employees group by department_id 
having c > 10;
-- Получение максимальной зарплаты по каджому депортаменту
select first_name, last_name, job_id, salary, max_salary as by_dep, hire_date
from employees as e
inner join ( 
select department_id, max(salary) as max_salary
from employees
group by department_id
) as dep_salary
on e.department_id = dep_salary.department_id
where e.dep_salary = dep_salary.max_salary
order by e.salary DESC;
select d.department_name, e.first_name, e.last_name, e.job_id, max(e.salary), e.hire_date
from employees as e
join departments as d
on d.department_id = e.department_id
group by d.department_name;


SELECT
*
FROM
departments d
WHERE
department_id in 
(
SELECT
e.department_id
from
employees e
group by
department_id
having
COUNT(department_id) = 
(
SELECT
max(cnt_emp)
FROM
(
SELECT
department_id,
count(employee_id) as cnt_emp
from
employees e
group by
department_id
order by
cnt_emp desc
) as tb1
)
)
;
select d.department_id, d.department_name, count(e.employee_id) as count_emp, d.manager_id
from departments as d
inner join employees as e
on d.department_id = e.department_id
group by d.department_id
order by count_emp desc
limit 1;

select t1.department_name, t1.manager_id, t2.count_of_emp
from departments as t1
join (
select department_id, count(employee_id) as count_of_emp
from employees
group by department_id
having count_of_emp > 10

) as t2
 on t1.department_id = t2.department_id;
 -- Подключиться к базе данных world
use world;
-- 2. Вывести население в каждой стране (CountryCode, sum(Population))
SELECT CountryCode, SUM(Population) AS total_population
FROM city
GROUP BY CountryCode;
--  3. Вывести только страны с населением более 3 млн человек
SELECT CountryCode, SUM(Population) AS total_population
FROM city
GROUP BY CountryCode
HAVING SUM(Population) > 3000000;
-- 4. Сколько всего записей в результате?
SELECT COUNT(*)
FROM (
    SELECT CountryCode, SUM(Population) AS total_population
    FROM city
    GROUP BY CountryCode
    HAVING SUM(Population) > 3000000
) AS result;
-- Поменять запрос так, чтобы выводилось название страны вместо кода (JOIN с таблицей country)
SELECT co.Name AS CountryName, SUM(ci.Population) AS total_population
FROM city ci
JOIN country co ON ci.CountryCode = co.Code
GROUP BY co.Name
HAVING SUM(ci.Population) > 3000000;
-- Вывести количество городов в каждой стране (CountryCode, amount of cities). (Подсказка: запрос по таблице city и группировка по CountryCode)
SELECT CountryCode, COUNT(Name) AS city_count
FROM city
GROUP BY CountryCode;
-- Поменять запрос так, чтобы вместо кодов стран, было названия стран. 
SELECT co.Name AS CountryName, COUNT(ci.Name) AS city_count
FROM city ci
JOIN country co ON ci.CountryCode = co.Code
GROUP BY co.Name;
-- Поменять запрос так, чтобы выводилось среднее количество городов в стране. Подсказка: разделите задачу на несколько подзадач. Например, сначала вывести код страны и количество городов в каждой стране.  Затем сделать join получившегося результата с запросом, где высчитывается среднее от количества городов. Потом добавить join, который добавит имена стран, вместо кода. 
select floor(avg(cc.city_count)) as average_cities
from (
select CountryCode, count(Name) as city_count
from city
group by CountryCode
) as cc;