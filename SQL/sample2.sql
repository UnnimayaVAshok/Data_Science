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
insert into employee(f_name,l_name,age,email,gender)values("Arun","S",22,"a@gmail.com","male"),
														  ("Amal","R",25,"ab@gmail.com","male"),
                                                          ("Rahul","A",26,"r@gmail.com","male");
insert into employee(f_name,l_name,age,email,gender)values("Arya","R",20,"arya@gmail.com","female");
select f_name,status,email from employee where id = 2;