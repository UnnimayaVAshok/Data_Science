create database student_db;
use student_db;
create table student_details(id int auto_increment primary key,
							f_name varchar(30) not null,
                            l_name varchar(30),
                            age int,
                            gender enum("male","female","other"),
                            course enum("Data Science","Web Development","Data Analyst"),
                            city varchar(20) not null,
                            email varchar(30) unique,
                            phn varchar(15) unique,
                            admission_date date,
                            status enum("active","inactive") default "active");
insert into student_details(f_name,l_name,age,gender,course,city,email,phn,admission_date)
					values("Arya","S",18,"female","Data Science","Kochi","arya@gmail.com","9033547688","2026-02-12");
insert into student_details(f_name,l_name,age,gender,course,city,email,phn,admission_date,status)
					values("Amal","R",20,"male","Data Science","Kollam","amal@gmail.com","9833547688","2026-02-15","inactive"),
                    ("Rahul","R",19,"male","Data Analyst","Kottayam","rahul@gmail.com","9888547688","2026-02-14","active"),
                    ("Aswathy","P",20,"female","Web Development","Kollam","aswathy@gmail.com","9833587688","2026-02-15","active"),
                    ("Sania","A",22,"female","Data Analyst","Kochi","sania@gmail.com","9833549588","2026-02-15","active");
insert into student_details(f_name,l_name,age,gender,course,city,email,phn,admission_date)
					values("Amisha","S",18,"female","Data Science","Kozhikode","amisha@gmail.com","9233547688","2026-02-10");
		select * from student_details;
        select f_name,course,city from student_details;
        select f_name from student_details where course = "Data Science";
        select f_name from student_details where age > 20;
        select f_name from student_details where city = "kochi";
