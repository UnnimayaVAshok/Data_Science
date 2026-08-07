create database college_db;
use college_db;
create table department(dept_id int auto_increment primary key,
						dept_name enum("mech","cse","eee","AI"),
                        hod varchar(50));
                        
create table student(student_id int auto_increment primary key,
					student_name varchar(30),
                    student_age int,
                    department_id int,
                    foreign key (department_id) references department(dept_id));
                    
insert into department(dept_name,hod)values("mech","shanu"),
											("cse","manu"),
                                            ("eee","milan"),
                                            ("AI","Anugrah");
                                            
insert into student(student_name,student_age,department_id)values("aswin",21,1),
																("sanu",22,1),
                                                                ("akshara",22,2),
                                                                ("amrutha",20,3),
                                                                ("varun",19,2);
select * from department;
select * from student;

select * from department,student;

select student_name,dept_name,student_age from student join department on student.department_id = department.dept_id;

truncate department;
drop table student;
drop table department;

select student_name,dept_name from student join department on student.department_id = department.dept_id where dept_name = "cse";
select count(student_name)  from student join department on student.department_id = department.dept_id where dept_name = "cse";
select dept_name,student_name from department left join student on student.department_id = department.dept_id;