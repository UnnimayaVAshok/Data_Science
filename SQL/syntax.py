"""
create database databasename;
use databasename;
create table tablename(column_name datatype constraints);

select column_name from tablename;
select * from tablename;

describe tablename;

insert into tablename(column1_name,column2_name,.........)values(column1_value,column_value,.......),
                                                                (column1_value,column_value,.......);

select * from tablename where condition;   

alter table tablename rename column column_name to new_column_name;
alter table tablename modify email varchar(100);
alter table tablename add salary decimal(10,2) default 5000;
alter table tablename drop column salary;

update tablename set age = 26 where id = 1;

update tablename set email = "amal@gmail.com" where id = 2;
update tablename set f_name = "Vinay",l_name = "K",age = 32,email = "v@gmail.com" where id = 2;
delete from tablename where id = 3;

delete from tablename;
truncate table tablename;

update tablename set age = null where id = 4;

alter table tablename rename to new_tablename;

=,<=,>=,!= (<>)

operators 
================
and
or
====================

keywords
=================
between value1 and value2

order by 
===============
is used to sort the result set of a query in either ascending or descneding order

default - ascending 

limit
================
is used to restrict the number of records returned by a query


Aggregate functions
==========================
count()         select count(*) from table_name;
                select count(*) from table_name where condition;
                select count(*) as column_name from table_name where condition;

sum()           select sum(column_name) as new_name from tablename where condition;

avg()           select avg(column_name) as new_name from tablename where condition;

max()           select max(column_name) as new_name from tablename where condition;

min()           select min(column_name) as new_name from tablename where condition;


subquery
===========
select name,mark from academics where mark = (select max(mark) from academics);

select name,mark from academics where mark > (select avg(mark) from academics);

like
=============
select name from academics where name like '%a';
select name from academics where name like 'a%'; 

primary key
=================
a primary key uniquely identifies each row within a single database table

foreign key
=================
Foreign key links data between two tables by referencing the primary key of another table

foreign key setting
======================
foreign key (current_table_column_name) references other_table_name(primary_column_name);

relationships
=============
one to many - foreign key default
one to one
many to many
many to one


joins - default inner join
=========
inner join - only rows that heve matching values in both tables

left join - all rows from the left table,plus matched rows from the right table.
            unmatched right rows return null,

right join - all rows from the right table,plus matched rows from the left table

outer join - all rows and records from both tables.

group by
==============
is used to combine rows having the same value into groups,so we can perform calculation on each group

"""
