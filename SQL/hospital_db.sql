create database hospital_db;
use hospital_db;
create table doctor(id int auto_increment primary key,
					name varchar(20),
                    specialized varchar(30),
                    experience int);
create table patient(id int auto_increment primary key,
					name varchar(20),
                    age int,
                    disease varchar(30),
                    bill_amount int,
                    doctor_id int,
                    foreign key(doctor_id) references doctor(id) on delete cascade);

insert into doctor(name,specialized,experience)values("Arun","psych",4),
													("Rahul","dental",3),
                                                    ("Amal","surgeon",5);
insert into patient(name,age,disease,bill_amount,doctor_id)values("Vinay",23,"fever",1200,1),
																("Suraj",22,"surgery",5000,3),
                                                                ("Ram",25,"checkup",6000,2);
insert into patient(name,age,disease,bill_amount,doctor_id)values("Nivedh",23,"fever",1200,1);
drop table patient;
select * from doctor;
select * from patient;
select doctor_id,count(*) as total from patient group by doctor_id;
select doctor_id,sum(bill_amount) as total_bill from patient group by doctor_id;
select doctor_id,avg(bill_amount) as avg_bill from patient group by doctor_id; 
select doctor_id,max(bill_amount) as highest from patient group by doctor_id;
select doctor.name,count(patient.id) as total_patience from doctor join patient on doctor.id = patient.doctor_id group by doctor_id;

select disease,count(id) as total_patience from patient group by disease;
select disease,sum(bill_amount) as total_amount from patient group by disease;
select disease,max(bill_amount) as max_amount from patient group by disease;
select disease,min(bill_amount) as min_amount from patient group by disease;
select disease,avg(bill_amount) as avg_amount from patient group by disease;

insert into patient(name,age,disease,bill_amount,doctor_id)values("Niva",23,"cold",1000,1);
select doctor_id,disease,count(*) as total_patience from patient group by doctor_id,disease;
select doctor_id,disease,sum(bill_amount) as total_bill from patient group by doctor_id,disease;
select doctor_id,disease,avg(bill_amount) as avg_bill from patient group by doctor_id,disease;
select doctor_id,disease,max(bill_amount) as max_amount from patient group by doctor_id,disease;
select doctor_id,disease,min(bill_amount) as min_amount from patient group by doctor_id,disease;