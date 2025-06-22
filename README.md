# Project: Best-buy App

A command-line interface (CLI) store simulator written in Python. This application allows users to view products, check inventory, and place orders — all through an interactive terminal-based menu.

---

## 📦 Features

- View a list of all available products.
- Display the total quantity of items in store.
- Add multiple products to a shopping cart and place an order.
- Supports different product types:
  - **Regular Products**
  - **Non-Stocked Products**
  - **Limited Products** (with max quantity constraints)
- Promotions available:
  - **Second Half Price**
  - **Third One Free**
  - **30% Discount**

---

Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit


## 📁 Project Structure
```plaintext
best-buy/
├── main.py
├── store.py
├── products.py
├── promotions.py
├── tests/
│   ├── test_store.py
│   └── test_products.py
    └── test_promotions.py
├── pytest.ini
```

## 🚀 How to Run
1. **To install this project, Clone the Repository:**


    `git clone https://github.com/spKnowTech/best-buy.git`
    
    `cd best-buy`
2. **Create a Virtual Environment (Optional but Recommended):**


    `python -m venv venv`
    
    `source venv/bin/activate` # On Windows: venv\Scripts\activate
3. **Install Dependencies:**


    `pip install pytests`

## Run Tests

Open the terminal in your project directory and Type `pytests`

## 🚀 Usage

1. **To use this project, Run the following command:**


    `python main.py`


## ✨ Sample Output
```plaintext
1. MacBook Air M2, Price: 1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500
3. Google Pixel 7, Price: 500, Quantity: 250


🟦 Total of 1100 items in store. 🟦

✅ Order made! Total payment 💰: $1700 ✅
```

## 📌 Notes
- To finish an order during product selection, simply press Enter without typing a product number or quantity.
- The program validates inputs and handles edge cases (e.g., invalid selections, out-of-stock errors).

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.