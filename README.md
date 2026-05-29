# Vegetable Management System

## Overview

Vegetable Management System is a Python and MySQL based application used to manage vegetable inventory, sales, billing, and profit reports. The system provides separate access for Owner and User operations.

## Technologies Used

- Python
- MySQL
- MySQL Connector

## Features

### Owner Module
- Secure Login
- Add Vegetables
- Delete Vegetables
- Update Quantity and Prices
- View Inventory
- Item Wise Profit Report
- Sales Report

### User Module
- View Available Vegetables
- Add Items to Cart
- Modify Cart
- Remove Items from Cart
- Generate Bill
- Purchase Management

## Database Tables

### Owner
- Vegetables
- Quantity
- Cost Price
- Sell Price
- Sold Quantity

### User
- Item Name
- Item Quantity
- Item Price

## Project Structure

- `vegetable_management_system.py` - Main application file

## How to Run

1. Install Python
2. Install MySQL
3. Install MySQL Connector

```bash
pip install mysql-connector-python
```

4. Create required database and tables in MySQL
5. Update database credentials in the source code
6. Run the program

```bash
python vegetable_management_system.py
```

## Author

Kiran Kumar
