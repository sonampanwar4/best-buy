# Project: Best-buy App

## 📌 Features
- A Product class includes an attribute to keep track of the total quantity of items of that product currently 
available in the store. When someone will purchase it, the amount will be modified accordingly.
- A Store class which will hold all of these products, and will allow the user to make a purchase of 
multiple products at once.
- A user interface (CLI) for managing the store

## 📁 Project Structure
```plaintext
best-buy/
├── static/
│   ├── index_template.html
│   └── style.css
├── main.py
├── store.py
├── products.py
├── tests/
│   ├── test_store.py
│   └── test_products.py
├── pytest.ini
```

## 🛠️ Installation
1. **To install this project, Clone the Repository:**


    `git clone https://github.com/spKnowTech/best-buy.git`
    
    `cd best-buy`
2. **Create a Virtual Environment (Optional but Recommended):**


    `python -m venv venv`
    
    `source venv/bin/activate` # On Windows: venv\Scripts\activate
3. **Install Dependencies:**


    `pip install pytests`

## 🛞 Functionalities Tests
- Ordering a quantity too large
- Product that runs out of stock
- Products that is created with invalid parameters

## Run Tests

Open the terminal in your project directory and Type `pytests`

## 🚀 Usage

1. **To use this project, Run the following command:**


    `python main.py`