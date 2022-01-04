-- Your solution here
select capital from countries where continent like 'Afri%a'
and country like 'E%' order by capital limit 3;