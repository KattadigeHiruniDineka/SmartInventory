# 📦 StockSmart — Smart Inventory Management System

StockSmart is a simple and user-friendly inventory management web application developed using Python and Streamlit. It helps users manage products, track stock quantities, record sales, restock products, and identify low-stock items.

## ✨ Features

- 📊 **Dashboard** — View product statistics and total stock value.
- ➕ **Add Products** — Add new products with IDs, names, prices, quantities, and categories.
- 🛍️ **Sales Management** — Record product sales and automatically update stock quantities.
- 📦 **Restock Management** — Increase stock quantities for existing products.
- ⚠️ **Low-Stock Alerts** — Identify products with low stock levels.
- 🔍 **Product Search** — Find products using their names or IDs.
- ✅ **Success and Error Messages** — Receive feedback after completing actions.
- 🎨 **User-Friendly Interface** — Simple green-and-white design.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Object-Oriented Programming (OOP)

## 🧠 OOP Concepts Used

### 1. Encapsulation

Encapsulation is used in the `Product` class to control access to product prices and quantities. Properties and setter methods validate values before updating them.

### 2. Inheritance

Inheritance is implemented through the `Electronics` and `Grocery` classes, which inherit common attributes and methods from the `Product` class.

## 📁 Project Structure

```text
SmartInventory/
├── app.py
├── product.py
├── inventory.py
├── requirements.txt
└── README.md
```

## 🚀 Installation and Setup

### Prerequisites

- Python installed on your computer
- Git installed on your computer

### Step 1: Clone the Repository

```bash
git clone https://github.com/KattadigeHiruniDineka/SmartInventory.git
```

### Step 2: Navigate to the Project Folder

```bash
cd SmartInventory
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python -m streamlit run app.py
```

### Step 5: Open the Application

Open the local URL displayed in your terminal. Usually:

```text
http://localhost:8501
```

## 📌 Future Improvements

- Store inventory data permanently using a database.
- Generate sales reports.
- Add user authentication.
- Export inventory reports to CSV or PDF.
- Add product expiry-date tracking.

## ⚠️ Current Limitations

This version uses Streamlit session state to manage inventory data. Data is not stored in a permanent database, so it may not persist between sessions.

## 👩‍💻 Author

**Developed as a Python Object-Oriented Programming project.**

## 📄 License

This project is intended for educational purposes.
