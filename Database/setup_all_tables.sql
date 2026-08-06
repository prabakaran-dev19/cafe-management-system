-- ============================================================
-- Cafe Management System - Full DB Setup (FINAL, FIXED VERSION)
-- Run this single file for a fresh setup, or on top of an existing
-- DB — it drops and recreates everything so it's always correct.
-- ============================================================

CREATE DATABASE IF NOT EXISTS cafe_management_system;
USE cafe_management_system;

DROP TABLE IF EXISTS MENU_ITEMS;
DROP TABLE IF EXISTS ORDERS;
DROP TABLE IF EXISTS CUSTOMER;
DROP TABLE IF EXISTS EMPLOYEE;

-- ---------------- MENU_ITEMS ----------------
CREATE TABLE MENU_ITEMS (
    ITEM_ID     VARCHAR(20) PRIMARY KEY,
    ITEM_NAME   VARCHAR(100) NOT NULL,
    PRICE       DECIMAL(10,2) NOT NULL,
    CATEGORY    VARCHAR(50) NOT NULL,
    DESCRIPTION VARCHAR(255),
    IMAGE_URL   VARCHAR(255)
);

-- ---------------- CUSTOMER ----------------
CREATE TABLE CUSTOMER (
    CUST_NAME  VARCHAR(100) NOT NULL,
    MOBILE_NO  VARCHAR(15) PRIMARY KEY,
    ADDRESS    VARCHAR(255),
    PSWD       VARCHAR(100) NOT NULL
);

-- ---------------- EMPLOYEE ----------------
-- EMP_ID is VARCHAR (form allows text IDs like "E101")
-- GENDER is VARCHAR(10) (form sends full word "Male"/"Female"/"Other")
CREATE TABLE EMPLOYEE (
    EMP_NAME     VARCHAR(100) NOT NULL,
    EMP_ID       VARCHAR(20) PRIMARY KEY,
    DESIGNATION  VARCHAR(50),
    GENDER       VARCHAR(10),
    MOB_NO       VARCHAR(15),
    EMAIL        VARCHAR(100),
    PSWD         VARCHAR(100)
);

-- ---------------- ORDERS ----------------
CREATE TABLE ORDERS (
    ORDER_NO   INT AUTO_INCREMENT PRIMARY KEY,
    ITEM_NAME  VARCHAR(100),
    ITEM_NO    VARCHAR(20),
    MOB_NO     VARCHAR(15),
    QUANTITY   INT
);

-- ============================================================
-- Seed data
-- ============================================================

-- Menu items — IDs match the hardcoded item_key values used in
-- coffeemenu.html, pizzamenu.html, burgers.html, Sandwiches.html,
-- Beverages.html, shorteates.html. IMAGE_URL matches the exact
-- (case-sensitive) filenames in static/images.
INSERT INTO MENU_ITEMS (ITEM_ID, ITEM_NAME, PRICE, CATEGORY, DESCRIPTION, IMAGE_URL) VALUES
-- Coffee
('item2',  'Americano', 110, 'Coffee', 'Hot water poured over Rainforest Alliance Certified espresso.', 'Americano.jfif'),
('item3',  'Cappuccino', 120, 'Coffee', 'Whole steamed milk, bold espresso, foamed milk.', 'Cappuccino.png'),
('item17', 'Filter Coffee', 90, 'Coffee', 'Classic South Indian style Filter Coffee.', 'FIltercoffee.jpg.png'),
('item18', 'Cafe Latte', 130, 'Coffee', 'Rich espresso brewed with steamed milk.', 'CafeLatte.png'),
('item19', 'Cold Coffee', 140, 'Coffee', 'Freshly brewed cold coffee, chilled.', 'Coldcoffee.jpg'),
('item20', 'Hot Velvet Coffee', 150, 'Coffee', 'Trendy Dalgona coffee in a new avatar.', 'Dalgonacoffeejpg.jpg'),

-- Pizza
('item6',  'Margherita (Veg)', 220, 'Pizza', 'Classic cheese and tomato pizza.', 'Margherita.jpg'),
('item7',  'Farmhouse (Veg)', 260, 'Pizza', 'Loaded with fresh veggies.', 'Farmhouse.jpg'),
('item8',  'Chicken Dominator (Non-Veg)', 300, 'Pizza', 'Loaded with spicy chicken toppings.', 'Chickend.jpg'),
('item21', 'Chicken Fiesta (Non-Veg)', 290, 'Pizza', 'Topped with grilled chicken.', 'ChickenPizza.jpg'),

-- Burgers
('item9',  'Gourmet DoubleDecker Paneer Burger (Veg)', 150, 'Burgers', 'Double paneer patty burger.', 'Paneerdouble.jpg'),
('item10', 'Gourmet DoubleDecker Chicken Burger (Non-Veg)', 170, 'Burgers', 'Double chicken patty burger.', 'Chicken.jpg'),
('item11', 'American Grilled Cheese Burger (Veg)', 130, 'Burgers', 'Loaded with melted cheese.', 'Americancheese.png'),

-- Sandwiches
('item4',  'Grilled Paneer Sandwich (Veg)', 100, 'Sandwiches', 'Grilled paneer sandwich.', 'Sandwiches.jpg'),
('item5',  'Grilled Chicken Sandwich (Non-Veg)', 110, 'Sandwiches', 'Grilled chicken sandwich.', 'Chicken-Grilled-sandwich-1.jpg'),
('item22', 'Morrocon Sandwich (Non-Veg)', 120, 'Sandwiches', 'Spiced Moroccan style sandwich.', 'Morrocon.png'),

-- ShortEats
('item15', 'Premium Paneer Wrap (Veg)', 90, 'ShortEats', 'Spiced paneer wrap.', 'paneer-roll.jpg'),
('item16', 'Chicken Wrap (Non-Veg)', 100, 'ShortEats', 'Spiced chicken wrap.', 'Chickenroll.png'),
('item23', 'Mexican Nuggets (Non-Veg)', 120, 'ShortEats', 'Crispy Mexican style nuggets.', 'Chicken-Nuggets.jpg'),

-- Beverages
('item12', 'Fresh Fruit Juice', 70, 'Beverages', 'Freshly squeezed fruit juice.', 'Fruit.jpg'),
('item13', 'Milkshakes', 100, 'Beverages', 'Thick creamy milkshake.', 'Milkshakes.jpg'),
('item14', 'Packaged Mineral Water', 20, 'Beverages', 'Packaged drinking water.', 'Water.png');

-- Sample employees (Employee ID is text now, e.g. "E101")
INSERT INTO EMPLOYEE (EMP_NAME, EMP_ID, DESIGNATION, GENDER, MOB_NO, EMAIL, PSWD) VALUES
('LUCAS MOORE','E101','CHEF','Male','7799301156','luc123@gmail.com','luc123'),
('SIA GREEN','E102','WAITER','Female','9123087436','sia123@gmail.com','sia123'),
('SIMONA LOBO','E103','WAITER','Female','7663320993','sim123@gmial.com','sim123'),
('DAISY','E104','HELPER','Female','4569871023','dai@gmail.com','dai123'),
('LILY','E105','HELPER','Female','9865740123','lil@gmail.com','lil123');