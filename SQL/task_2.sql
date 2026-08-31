create database company_new_db;
use company_new_db;
create table departments(department_id int auto_increment primary key,
						departmant_name varchar(50),
                        location varchar(50));
alter table departments rename column departmant_name to department_name;
insert into departments(department_name,location) values("IT","Kochi"),
														("HR","Trivandrum"),
                                                        ("Finance","Kochi"),
                                                        ("Marketing","Calicut"),
                                                        ("Sales","Thrissur");
select * from departments;
create table employees(employee_id int primary key,
						employee_name varchar(50),
                        age int,
                        salary decimal(10,2),
                        experience int,
                        city varchar(50),
                        department_id int,
                        foreign key (department_id) references departments(department_id));
insert into employees(employee_id,employee_name,age,salary,experience,city,department_id) values(101,"Arun",25,35000,2,"Kochi",1),
																								(102,"Meera",29,48000,5,"Trivandrum",1),
                                                                                                (103,"Rahul",32,55000,8,"Kochi",3),
                                                                                                (104,"Anjali",27,42000,4,"Calicut",4),
                                                                                                (105,"Vishnu",35,65000,10,"Thrissur",5),
                                                                                                (106,"Sneha",24,30000,1,"Kochi",2),
                                                                                                (107,"Nikhil",31,52000,7,"Trivandrum",1),
                                                                                                (108,"Athira",28,45000,5,"Kochi",3),
                                                                                                (109,"Suresh",40,75000,15,"Thrissur",5),
                                                                                                (110,"Diya",26,38000,3,"Calicut",4),
                                                                                                (111,"Amal",30,50000,6,"Kochi",1),
                                                                                                (112,"Fathima",33,60000,9,"Trivandrum",2),
                                                                                                (113,"Kiran",29,47000,5,"Kochi",3),
                                                                                                (114,"Neethu",27,41000,3,"Calicut",4),
                                                                                                (115,"Joel",36,68000,11,"Thrissur",5);
select * from employees;
select employee_name,salary,city from employees;
select employee_name from employees where salary > 50000;
select employee_name from employees where experience > 5;
select employee_name from employees where age between 25 and 30;
select distinct city from employees;
select distinct department_id from employees;
select distinct city,department_id from employees;
select employee_name,department_name from employees as e join departments as d on e.department_id=d.department_id;
select employee_name,salary,department_name from employees as e join departments as d on e.department_id=d.department_id;
select employee_name,department_name from employees as e join departments as d on e.department_id=d.department_id where d.department_name="IT";
select employee_name,department_name from employees as e join departments as d on e.department_id=d.department_id where e.city="Kochi";
select department_name,count(*) from departments as d join employees as e on d.department_id=e.department_id group by e.department_id;
select department_name from departments as d join employees as e on d.department_id=e.department_id group by e.department_id having count(*) > 2;
select department_name,avg(salary) from departments as d join employees as e on d.department_id=e.department_id group by e.department_id;
select department_name from departments as d join employees as e on d.department_id=e.department_id group by e.department_id having avg(salary) > 50000;
select department_name from departments as d join employees as e on d.department_id=e.department_id group by e.department_id having max(salary) > 60000;
select employee_name from employees order by salary desc limit 5;
select employee_name from employees order by salary  limit 3;
select employee_name from employees order by employee_name limit 5;
select employee_name from employees where salary > (select avg(salary) from employees);
select employee_name from employees where salary = (select max(salary) from employees);
select employee_name from employees where experience > (select avg(experience) from employees);
select employee_name from employees where department_id = (select department_id from employees where employee_name = "Arun");
select employee_name from employees where salary > (select salary from employees where employee_name = "Anjali");