import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin@1234',
    database = 'tesla'
    )

c = mydb.cursor()

# c.execute('CREATE DATABASE tesla')

c.execute("""create table car(
	car_id integer not null,
	name varchar(100) not null,
    model varchar(150) not null,
    color varchar(100) not null,
    price integer not null,
    f_customer_id integer not null,
    primary key(car_id),
    FOREIGN KEY (f_customer_id) REFERENCES tesla.customer(customer_id)
);""")


#=========================================================

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@1234",
    database="tesla"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")