create database shopping_db;
use shopping_db;
create table Product(product_id int auto_increment primary key,
					product_name varchar(20) not null,
                    category enum("Electronics","Grocery","Clothing"),
                    price int not null,
                    stock int,
                    rating decimal(1,1));
alter table Product modify rating decimal(2,1);
describe  Product;
select * from Product;
insert into Product(product_name,category,price,stock,rating)values("Laptop","Electronics",65000,15,4.7),
																	("Smartphone","Electronics",25000,30,4.5),
                                                                    ("Rice bag","Grocery",850,40,4.2),
                                                                    ("T-shirt","Clothing",799,50,4.0),
                                                                    ("Bluetooth speaker","Electronics",3500,12,4.3),
                                                                    ("Oil","Grocery",220,60,4.1),
                                                                    ("Jeans","Clothing",1800,18,4.4),
                                                                    ("Refrigetaror","Electronics",42000,8,4.8);
select product_name,price from Product;
select category,stock from product;
select * from Product where price > 5000;
select * from Product where price < 1000;
select * from Product where price between 1000 and 5000;
select * from Product where stock > 20;
select * from Product where rating > 4;
select * from Product where category = "Electronics" and rating > 4;
select * from Product where category = "Grocery" or category = "Clothing";
select product_name,rating from Product where stock < 15;
update Product set price = 60000 where product_id = 1;
update Product set stock = 30 where product_id = 3;
update Product set category = "Clothing" where product_id = 3;
alter table Product add column brand varchar(20); 
alter table Product rename column product_name to item_name;
alter table Product modify item_name varchar(25);
alter table Product rename to Product_details;
select * from Product_Details;
delete from Product_Details where product_id = 4; 
alter table Product_Details drop rating;
drop table Product_Details;
drop database shopping_db;