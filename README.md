# 🛒 Inventory Management System (Python)

A console-based Python program that helps shops manage product stock, handle sales, and keep records organized using file operations. Designed with simplicity and real-world functionality in mind.

---

## 🧩 Key Components

### 📦 Product
Each item in the shop is represented as a product, including:
- Name
- Brand
- Price
- Quantity in stock
- Origin (where it comes from)

### 📋 Inventory
Acts as the product collection manager:
- Tracks available stock
- Updates when items are sold or restocked
- Can search and retrieve product details quickly

### 📁 Product File Operations
Ensures data persistence through file I/O:
- **Read**: On startup, the program loads all product data from a text file (e.g. `products.txt`)
- **Write**: On any change (sale, restock, add), the file is updated to maintain accurate records

### 🛍️ Sales & Restocking Logic
- Automates sales processing and applies deals like **"Buy 3 Get 1 Free"**
- Generates customer bills
- Updates inventory automatically
- Easily adds new stock or restocks existing items

### 🖥️ User Interface
- Menu-driven CLI (Command Line Interface)
- Simple navigation for:
  - Viewing all products
  - Searching by name or brand
  - Selling items
  - Restocking
  - Updating product info

---

## 🛠️ Built With
- 🐍 **Python**
- 📁 File Handling (`open()`, `readlines()`, `write()`)
- 🧠 Logical conditions and modular functions

---
