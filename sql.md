CREATE DATABASE food_delivery_db;
show databases;
use food_delivery_db;
select database();
create table customers( 
  customer_id int primary key auto_increment,
  customer_name varchar(100) not null, 
  age int not null,
  email varchar(100) not null unique , 
  phone varchar(12) not null unique, 
  address text, 
  account_status ENUM('ACTIVE','NOT ACTIVE') not null default 'ACTIVE', 
  constraint check_age check (age > 18)
);
create table restaurant_table( 
    restaurant_id int primary key auto_increment,
    city varchar(50),
    rating int default 0,
    status enum('OPENED','CLOSED') not null
);
create table food_items(
  food_id int primary key auto_increment, 
  food_name varchar(50) not null, 
  restaurant_id int not null, 
  category varchar(50), 
  price decimal(10,2), 
  availability varchar(20) default 'AVAILABLE' , 
  foreign key(restaurant_id) references restaurant_table(restaurant_id) 
);
create table orders( 
  order_id int primary key auto_increment, 
  customer_id int not null ,
  order_date date default now(), 
  order_status varchar(20),  
  total_amount decimal(10,2), 
  foreign key(customer_id) references customers(customer_id) 
);
create table order_items( 
  order_item_id int primary key auto_increment, 
  order_id int not null, 
  food_id int not null,
  quantity int, 
  price decimal(10,2), 
  foreign key(order_id) references orders(order_id), 
  foreign key(food_id) references food_items(food_id)
);
INSERT INTO customers (customer_name, email, phone, address, age, account_status)
    VALUES
    ('Ravi',  'ravi@gmail.com',  '9876543210', 'Hyderabad', 24, 'ACTIVE'),
    ('Anil',  'anil@gmail.com',  '9876543211', 'Chennai',   29, 'ACTIVE'),
    ('Priya', 'priya@gmail.com', '9876543212', 'Bangalore', 22, 'ACTIVE'),
    ('Kiran', 'kiran@gmail.com', '9876543213', 'Hyderabad', 31, 'ACTIVE'),
    ('Sneha', 'sneha@gmail.com', '9876543214', 'Chennai',   27, 'ACTIVE'),
    ('Arjun', 'arjun@gmail.com', '9876543215', 'Pune',      35, 'NOT ACTIVE'),
    ('Neha',  'neha@gmail.com',  '9876543216', 'Hyderabad', 23, 'ACTIVE'),
    ('Vijay', 'vijay@gmail.com', '9876543217', 'Bangalore', 40, 'NOT ACTIVE');


# Sub queries 

sub querie is a querie that is written inside another querie

find food_items whose price is greater that the average food price
select food_name,price from food_items where price > (select avg(price) from food_items);

# Window Function 

A window function performs a calculation across related rows while retaining each row in the result 

function_name(expression) over (
  .........
)

## row_number() -> assings a unique number to every row 

select employee_name,department,salary 
row_number() over(
  order by salary desc 
)as row_num from employees;

## Rank():
  
if two employees have the same salary ,should they have the same Rank ? -> Yes 

## Dense_rank():

Dense_rank() alsot givs the same rank to equal values but id does not leave gaps

## Lag() 

now move away from ranking. lag looks at a previous row  if no previous row then the result will be null

## lead()

it is opposite to the lag() function
