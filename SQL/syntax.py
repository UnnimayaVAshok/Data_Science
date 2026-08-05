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

                              
"""