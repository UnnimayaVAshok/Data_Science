create database MovieStreamDB;
use MoviestreamDB;
create table Movies(Movie_id int primary key,
					Movie_name varchar(30),
                    Genre enum("Action","Romance","Thriller"),
                    Language enum("Tamil","Malayalam","Kannada","Hindi"),
                    Rating decimal(2,1),
                    Duration_min int,
                    Release_year int);
drop table Movies;
		insert into Movies(Movie_id,Movie_name,Genre,Language,Rating,Duration_min,Release_year)values(101,"Leo","Action","Tamil",8.2,164,2023),
																									(102,"Premalu","Romance","Malayalam",8.5,156,2024),
                                                                                                    (103,"KGF","Action","Kannada",8.4,168,2018),
                                                                                                    (104,"Drishyam","Thriller","Malayalam",8.6,160,2013),
                                                                                                    (105,"Jawan","Action","Hindi",7.4,169,2023),
                                                                                                    (106,"96","Romance","Tamil",8.5,158,2018);
select * from Movies;
select Movie_name,Rating from Movies;
select distinct Genre from Movies;
select distinct Language from Movies;
select Movie_name from Movies order by Rating desc limit 3;
select Movie_name from Movies order by Rating desc limit 2;
select Movie_name from Movies limit 3;
select Movie_name from Movies where Rating > 8.0;
select Movie_name from Movies where Release_year > 2020;
select Movie_name from Movies where Genre = "Action";
select Movie_name from Movies order by Rating desc;
select Movie_name from Movies order by Release_year;
select max(Rating) from Movies;
select min(Duration_min) from Movies;
select avg(Rating) from Movies;
select Genre,count(*) from Movies group by Genre;
select Language,avg(Rating) from Movies group by Language;
select Genre from Movies group by Genre having count(*) > 1;
select Language from Movies group by Language having count(*) > 1;