/*  SQL  */

select substr(project,1,x.commits) project , RIGHT(address ,x.contributors) address
 from (select * from repositories )x;