select id, name from departments
where  exists  (select department_id from sales where 
sales.department_id= departments.id and
price>98);