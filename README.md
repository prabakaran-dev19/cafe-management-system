# ☕ Cafe Management System

A full-stack web application built with **Flask** and **MySQL** to streamline daily cafe operations — dynamic menu browsing, cart-based ordering, automated billing, and an admin panel for complete menu control.

---

## 📌 Project Overview

The Cafe Management System lets customers browse a categorized menu, add items to a live cart, and check out to an auto-generated receipt — while giving admins full control to add, edit, and delete menu items in real time through a protected dashboard, with all data persisted in MySQL.

---

## 🛠️ Tech Stack

| Layer      | Technology                          |
|------------|--------------------------------------|
| Frontend   | HTML5, CSS3, Jinja2 Templating       |
| Backend    | Python (Flask)                       |
| Database   | MySQL (via Flask-MySQLdb)            |
| Session    | Flask session-based cart & auth      |

---

## 🚀 Key Features

### Customer Experience
- **Dynamic Menu** — Items are pulled live from MySQL and grouped by category (Coffee, Pizza, Burgers, Sandwiches, Short Eats, Beverages), so menu changes reflect instantly with no code edits.
- **Live Cart** — "Order Now" adds items to a session-based cart with a persistent, ever-visible cart badge showing item count in real time.
- **Cart Management** — View, remove items, and see a running grand total before checkout.
- **Automated Billing** — Checkout generates a clean, itemized receipt with quantities, unit prices, and grand total.
- **Customer Accounts** — Register and log in to place orders under a saved profile.

### Admin Experience
- **Protected Admin Dashboard** — Session-secured login gates access to all admin-only routes.
- **Menu Management (CRUD)** — Add, edit, and delete menu items (name, price, category, description, image) directly from the browser — changes go live across the site immediately.
- **Flexible Images** — Use a local image filename or paste an external image URL directly from the browser.
- **Operational Stats** — Dashboard cards for total employees, orders, and registered customers.
- **Employee & Customer Records** — View and manage staff and customer data.

---

## 📂 Project Structure

```
cafe-management-system/
│
├── static/
│   ├── css/            # Stylesheets per page
│   └── images/         # Menu item & UI images
│
├── templates/           # HTML pages (Jinja2)
│   ├── welcome.html
│   ├── menu.html
│   ├── category.html    # Dynamic category listing
│   ├── cart.html
│   ├── receipt.html
│   ├── admin_menu.html
│   └── admin_menu_form.html
│
├── app.py                    # Flask application & routes
├── setup_menu_table.sql      # Initial menu table + seed data
├── update_menu_table.sql     # Adds description/image columns
└── README.md
```

---

## 👨‍💻 Author

**Prabakaran M**
- GitHub: [@prabakaran-dev19](https://github.com/prabakaran-dev19)
- LinkedIn: [Prabakaran M](https://www.linkedin.com/in/prabakaran19/)