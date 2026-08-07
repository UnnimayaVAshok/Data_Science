create database Students_db;
use Students_db;

create table academics(id int auto_increment primary key,
						name varchar(30) not null,
                        age int,
                        place varchar(20),
                        email varchar(30),
                        mark int check(mark < 100),
                        gender enum("male","female","others"));
                        
insert into academics(name,age,place,email,mark,gender)values("Arya",17,"Kochi","arya@gmail.com",98,"female"),
															("Amisha",19,"Kollam","amisha@gmail.com",95,"female"),
                                                            ("Varun",17,"Kottayam","varun@gmail.com",78,"male"),
                                                            ("Sreelakshmi",16,"kochi","sree@gmail.com",68,"female"),
                                                            ("Lallu",16,"Tvm","lallu@gmail.com",88,"male"),
                                                            ("Amaya",16,"kochi","amaya@gmail.com",58,"female");
alter table academics modify email varchar(30) unique;
select * from academics;
alter table academics modify mark int check(mark <= 100);
describe academics;

select count(*) from academics;
select count(*) from academics where gender = "female";
select count(*) as female_count from academics where gender = "female";

select sum(mark) as total_marks from academics;
select count(*) from academics where mark > 80;

select avg(age) as avg_age from academics;
select avg(mark) as avg_mark from academics where gender = "male";

select max(mark) as Max_mark from academics;

select min(mark) as Min_mark from academics;

select name,mark from academics order by mark desc limit 1;
select name,mark from academics where mark = (select max(mark) from academics);
select name,mark from academics where mark = (select min(mark) from academics);

select name,age from academics where age = (select max(age) from academics);
select name,age from academics order by age desc limit 1;

select name,mark from academics where mark > (select avg(mark) from academics);

select name from academics where name like "%a";

