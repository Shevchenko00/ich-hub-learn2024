-- 1. Вывести количество городов для каждой страны. Результат должен содержать CountryCode, CityCount (количество городов в стране). Поменяйте запрос с использованием джойнов так, чтобы выводилось название страны вместо CountryCode. 
SELECT c.Name AS CountryName, COUNT(ct.ID) AS CityCount
FROM country c
JOIN city ct ON c.Code = ct.CountryCode
GROUP BY c.Name
ORDER BY CityCount DESC;
-- 2. Используя оконные функции, вывести список стран с продолжительностью жизнью и средней продолжительностью жизни. 
select Name, LifeExpectancy,
avg(LifeExpectancy) over() as avg_life
from country;
-- 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.
SELECT 
    Name, 
    LifeExpectancy, 
    DENSE_RANK() OVER (ORDER BY LifeExpectancy DESC) AS Rang
FROM 
    country;
-- 4. Используя ранжирующие функции, вывести третью страну с самой высокой продолжительностью жизни.
Select * from
(select Name, LifeExpectancy,
dense_rank() over (order by LifeExpectancy) as rang
from country) as t1
where rang = 3;