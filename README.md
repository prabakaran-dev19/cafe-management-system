☕ Cafe Management System
A full-stack web application designed to streamline daily cafe operations, menu management, order tracking, and billing efficiency.
� �

📌 Project Overview

The Cafe Management System helps cafe managers and staff manage orders, customize menus, track sales, and generate receipts seamlessly. Built with a responsive frontend and a lightweight Python Flask backend powered by MySQL.

🛠️ Tech Stack

Frontend: HTML5, CSS3, JavaScript (ES6+)
Backend: Python (Flask Framework)
Database: MySQL

🚀 Key Features

Interactive Dashboard: View total orders, daily revenue, and recent transactions at a glance.
Menu Customization: Easily manage items, categories (drinks, pastries, meals), and pricing.
Order Processing: Real-time table ordering and status updates (Pending/Completed).
Bill Generation: Automated order receipt generation for quick customer checkout.
Database Integration: Secure and efficient data handling with MySQL.

⚙️ Setup & Installation

Prerequisites
Make sure you have the following installed on your local machine:
Python 3.x
MySQL Server
1. Clone the Repository
git clone https://github.com/prabakaran-dev19/cafe-management-system.git
cd cafe-management-system

2. Set Up Virtual Environment (Optional but Recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install flask mysql-connector-python

4. Database Setup
Open your MySQL client (e.g., MySQL Workbench or Command Line).
Create a new database and import the provided schema:
CREATE DATABASE cafe_db;
USE cafe_db;
-- Run script/schema.sql here
Update database credentials in app.py or your config file.

5. Run the Application
python app.py
Open your browser and navigate to http://127.0.0.1:5000/.

📂 Project Structure

cafe-management-system/
│
├── static/          # CSS, JavaScript, and Images
├── templates/       # HTML Pages (Jinja2 Templates)
├── app.py           # Flask Main Application
├── config.py        # Database Configurations
├── schema.sql       # MySQL Database Schema
└── README.md        # Project Documentation

👨‍💻 Author

Prabakaran M
GitHub: @prabakaran-dev19
LinkedIn: Prabakaran M