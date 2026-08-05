create database company_db;
use company_db;
create table employee(id int auto_increment primary key,
						f_name varchar(20) not null,
                        l_name varchar(20),
                        age int check(age >= 18),
                        email varchar(30) unique,
                        gender enum("male","female","others"),
                        status enum("active","inactive") default "active");
select * from employee;
describe employee;
insert into employee(first_name,l_name,age,email,gender)values("Arun","S",22,"a@gmail.com","male"),
														  ("Amal","R",25,"ab@gmail.com","male"),
                                                          ("Rahul","A",26,"r@gmail.com","male");
insert into employee(first_name,l_name,age,email,gender)values("Arya","R",20,"arya@gmail.com","female");
select first_name,status,email from employee where id = 2;
alter table employee rename column first_name to f_name;
alter table employee modify email varchar(100);
alter table employee add salary decimal(10,2) default 5000;
alter table employee drop column salary;

update employee set age = 26 where id = 1;

update employee set email = "amal@gmail.com" where id = 2;
update employee set f_name = "Vinay",l_name = "K",age = 32,email = "v@gmail.com" where id = 2;
delete from employee where id = 3;

delete from employee;
truncate table employee;

update employee set age = null where id = 4;

alter table employee rename to employees;


insert into employees(f_name,l_name,age,email,gender)values("Amisha","R",22,"amisha@gmail.com","female"),
															("Amaya","T",20,"amaya@gmail.com","female"),
                                                            ("Alan","U",23,"amlan@gmail.com","male");
select * from employees;
select * from employees where age > 30;
select * from employees where gender = "male";
select f_name,age from employees where age < 30;
select * from employees where f_name = "arun";
                                                            
alter table employees add salary decimal(10,2) default 5000;

update employees set salary = 300000 where id = 2;
select * from employees where salary >= 30000;
select * from employees where salary != 300000;
select * from employees where salary <> 5000;

select * from employees where age > 21 and gender = "male";
select * from employees where age > 21 or gender <> "male";
select * from employees where age > 25 and age < 32;
select * from employees where age between 25 and 32;