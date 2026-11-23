# STOCKWISE – Intelligent Inventory Management System

**Inventory Optimization Using Fractional Knapsack and 0/1 Knapsack Algorithms**

## 1. Project Overview

STOCKWISE is a web-based inventory management system developed using Python and Flask. It uses the Knapsack Problem to select products under a limited storage capacity while maximizing total profit.

The project implements two algorithms:

1. **Fractional Knapsack (Greedy Algorithm):** Allows products to be selected partially.
2. **0/1 Knapsack (Dynamic Programming):** Allows products to be selected completely or rejected.

The system provides an interactive dashboard where users can view products, enter storage capacity and compare the results of both algorithms.

## 2. Objectives

- Develop an inventory optimization system.
- Select products according to their weight and profit.
- Implement the Greedy approach.
- Implement Dynamic Programming.
- Calculate maximum profit within a given capacity.
- Compare the performance and results of both algorithms.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Backend programming |
| Flask | Web application framework |
| HTML | Frontend structure |
| CSS | Dashboard styling |
| JavaScript | Interactive functionality |
| Jinja2 | Dynamic webpage rendering |
| VS Code | Code development |

## 4. Project Structure

```text
InventoryKnapsack/
│
├── app.py
│
├── knapsack.py
│
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

Visit:

http://127.0.0.1:5000/

The STOCKWISE dashboard will open in your browser.

9. How to Use the Application

Open the STOCKWISE application.

View the available inventory products.

Enter the required storage capacity.

Run the optimization.

View the Fractional Knapsack results.

View the 0/1 Knapsack results.

Compare the selected products and maximum profit.
