-- Replace with your SQL query
with cte as(
select date, count(1) "count" from(
select  cast(date_trunc('month', created_at) as date) "date"
from posts) det
group by date
order by date),
cte2 as (
select date,count,count-lag(count,1) over(order by date) "diff" from cte
  )
select date,count, 
round(cast(diff/(cast(lag(count,1) over(order by date)  as float))*100 as 
     numeric),1)|| '%' "percent_growth"
from cte2;