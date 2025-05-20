☕ Coffee Management System

A command-line-based Coffee Management System built with Python and MySQL. It allows Admins to manage inventory, staff, and customer orders, while Customers can view items and place orders.

---

 📌 Features

 🔐 Admin

 Login authentication
 Add/View/Update/Delete:

   Coffee items
   Staff details
   Customer orders
 Search functionality
 Billing system

 👤 Customer

 View available coffee items
 Place orders
 Generate bills

---

 🛠️ Tech Stack

 Language: Python 3
 Database: MySQL
 Libraries Used:

   `mysql.connector`

---

 🏁 Getting Started

 ✅ Prerequisites

 Python 3 installed
 MySQL Server installed and running
 `mysql.connector` Python package
  Install using:

  ```bash
  pip install mysql-connector-python
  ```

---

 ⚙️ Setup Instructions

1. Clone the Repository:

   ```bash
   git clone https://github.com/your-username/coffee-management.git
   cd coffee-management
   ```

2. Configure MySQL:

    Make sure you have a MySQL user with access.
    Create a database and table:

     ```sql
     CREATE DATABASE cafe;
     USE cafe;

     CREATE TABLE coffee (
       serial_no INT PRIMARY KEY,
       products VARCHAR(100),
       cost FLOAT
     );
     ```

3. Run the Script:

   ```bash
   python coffee.py
   ```

---


 🧑‍💻 Author

Nikunj Jain
[LinkedIn Profile](https://www.linkedin.com/in/nikunjjain29/)

