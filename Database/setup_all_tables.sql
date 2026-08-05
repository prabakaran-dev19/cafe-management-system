-- ============================================================
-- Cafe Management System - Full DB Setup
-- (README refers to setup_menu_table.sql / update_menu_table.sql,
--  but those files were not included in the zip, so this recreates
--  everything app.py needs, based on the queries in app.py)
-- ============================================================

CREATE DATABASE IF NOT EXISTS cafe_management_system;
USE cafe_management_system;

-- ---------------- MENU_ITEMS ----------------
CREATE TABLE IF NOT EXISTS MENU_ITEMS (
    ITEM_ID     VARCHAR(20) PRIMARY KEY,
    ITEM_NAME   VARCHAR(100) NOT NULL,
    PRICE       DECIMAL(10,2) NOT NULL,
    CATEGORY    VARCHAR(50) NOT NULL,
    DESCRIPTION VARCHAR(255),
    IMAGE_URL   VARCHAR(255)
);

-- ---------------- CUSTOMER ----------------
-- app.py inserts VALUES(Name, Phonenumber, Address, pswd) in that order
CREATE TABLE IF NOT EXISTS CUSTOMER (
    CUST_NAME  VARCHAR(100) NOT NULL,
    MOBILE_NO  VARCHAR(15) PRIMARY KEY,
    ADDRESS    VARCHAR(255),
    PSWD       VARCHAR(100) NOT NULL
);

-- ---------------- EMPLOYEE ----------------
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EMP_NAME     VARCHAR(100) NOT NULL,
    EMP_ID       INT PRIMARY KEY,
    DESIGNATION  VARCHAR(50),
    GENDER       CHAR(1),
    MOB_NO       VARCHAR(15),
    EMAIL        VARCHAR(100),
    PSWD         VARCHAR(100)
);

-- ---------------- ORDERS ----------------
CREATE TABLE IF NOT EXISTS ORDERS (
    ORDER_NO   INT AUTO_INCREMENT PRIMARY KEY,
    ITEM_NAME  VARCHAR(100),
    ITEM_NO    VARCHAR(20),
    MOB_NO     VARCHAR(15),
    QUANTITY   INT
);

-- ============================================================
-- Seed data
-- ============================================================

-- Sample menu items (edit/add more from the Admin dashboard later)
INSERT INTO MENU_ITEMS (ITEM_ID, ITEM_NAME, PRICE, CATEGORY, DESCRIPTION, IMAGE_URL) VALUES
('item1', 'CAPPUCCINO', 110, 'Coffee', 'Espresso with steamed milk foam', 'Cappuccino.png'),
('item2', 'AMERICANO', 120, 'Coffee', 'Espresso with hot water', 'Americano.jfif'),
('item3', 'CAFE LATTE', 130, 'Coffee', 'Espresso with steamed milk', 'CafeLatte.png'),
('item4', 'COLD COFFEE', 140, 'Coffee', 'Chilled coffee blended with ice cream', 'Coldcoffee.jpg'),
('item5', 'MARGHERITA', 220, 'Pizza', 'Classic cheese and tomato pizza', 'Margherita.jpg'),
('item6', 'FARMHOUSE', 260, 'Pizza', 'Loaded with fresh veggies', 'Farmhouse.jpg'),
('item7', 'CHICKEN PIZZA', 280, 'Pizza', 'Topped with grilled chicken', 'ChickenPizza.jpg'),
('item8', 'CHICKEN BURGER', 150, 'Burgers', 'Crispy chicken patty burger', 'Chicken.jpg'),
('item9', 'PANEER DOUBLE BURGER', 140, 'Burgers', 'Double paneer patty burger', 'Paneerdouble.jpg'),
('item10', 'GRILLED SANDWICH', 100, 'Sandwiches', 'Grilled chicken sandwich', 'Chicken-Grilled-sandwich-1.jpg'),
('item11', 'AMERICAN CHEESE SANDWICH', 90, 'Sandwiches', 'Loaded with cheese', 'Americancheese.png'),
('item12', 'CHICKEN NUGGETS', 130, 'ShortEats', 'Crispy fried chicken nuggets', 'Chicken-Nuggets.jpg'),
('item13', 'CHICKEN ROLL', 90, 'ShortEats', 'Spiced chicken wrap', 'Chickenroll.png'),
('item14', 'MILKSHAKE', 100, 'Beverages', 'Thick creamy milkshake', 'Milkshakes.jpg'),
('item15', 'WATER BOTTLE', 20, 'Beverages', 'Packaged drinking water', 'Water.png');

-- Sample employees (also available in insert.sql)
INSERT INTO EMPLOYEE VALUES('LUCAS MOORE',335073,'CHEF','M','7799301156','luc123@gmail.com','luc123');
INSERT INTO EMPLOYEE VALUES('SIA GREEN',335074,'WAITER','F','9123087436','sia123@gmail.com','sia123');
INSERT INTO EMPLOYEE VALUES('SIMONA LOBO',335075,'WAITER','F','7663320993','sim123@gmial.com','sim123');
INSERT INTO EMPLOYEE VALUES('DAISY',336081,'HELPER','F','4569871023','dai@gmail.com','dai123');
INSERT INTO EMPLOYEE VALUES('LILY',336082,'HELPER','F','9865740123','lil@gmail.com','lil123');