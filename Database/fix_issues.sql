USE cafe_management_system;

-- ============================================================
-- FIX 1: Employee table column types
-- (form allows text IDs like "E101" and full-word gender like "Male")
-- ============================================================
ALTER TABLE EMPLOYEE MODIFY EMP_ID VARCHAR(20);
ALTER TABLE EMPLOYEE MODIFY GENDER VARCHAR(10);

-- ============================================================
-- FIX 2: Replace menu items with the correct set that matches
-- the item_key values hardcoded in the category templates
-- (coffeemenu.html, pizzamenu.html, burgers.html, Sandwiches.html,
--  Beverages.html, shorteates.html)
-- ============================================================
DELETE FROM MENU_ITEMS;

INSERT INTO MENU_ITEMS (ITEM_ID, ITEM_NAME, PRICE, CATEGORY, DESCRIPTION, IMAGE_URL) VALUES
-- Coffee
('item2',  'Americano', 110, 'Coffee', 'Hot water poured over Rainforest Alliance Certified espresso.', 'Americano.jfif'),
('item3',  'Cappuccino', 120, 'Coffee', 'Whole steamed milk, bold espresso, foamed milk.', 'Cappuccino.png'),
('item17', 'Filter Coffee', 90, 'Coffee', 'Classic South Indian style Filter Coffee.', 'Filtercoffee.jpg.png'),
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