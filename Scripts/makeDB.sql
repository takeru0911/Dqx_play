create table item ( id INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(64) NOT NULL, design_id INT(11), category_id INT(11),primary key(id));
create table category (id int(11) NOT NULL AUTO_INCREMENT, category_name VARCHAR(64) NOT NULL, primary key(id));
create table material (id INT(11) NOT NULL AUTO_INCREMENT, material_name VARCHAR(64) NOT NULL, primary key(id));
create table design (id INT(11) NOT NULL AUTO_INCREMENT, item_id INT(11), material_id INT(11), num_material INT(11),primary key(id));
create table market_material (id INT(11) NOT NULL AUTO_INCREMENT, date DATETIME, price INT(20),exhibits INT(11), item_id INT(11) ,primary key(id));
create table market_item (id INT(11) NOT NULL AUTO_INCREMENT, stars INT(11),date DATETIME, price INT(20),exhibits INT(11), item_id INT(11) ,primary key(id));
