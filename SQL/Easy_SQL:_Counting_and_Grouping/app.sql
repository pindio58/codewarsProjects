/*  SQL  */
select race, count(1)from demographics group by race order by count(1) desc;