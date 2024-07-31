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
