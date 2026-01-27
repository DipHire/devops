# case study  : e-commerce ordering proceess: 
# requirements :
# validate product quantity 
# caluculate Toatal
# Generate Order Ids,

# Function to validate product quantity
# def validate_quantity(quantity):
#     if quantity <= 0:
#         return False
#     return True


# # Function to calculate total price using range()
# def calculate_total(price_per_item, quantity):
#     total = 0
#     for i in range(quantity):   # range() used here
#         total += price_per_item
#     return total


# # Function to generate Order ID
# def generate_order_id(order_number):
#     return f"ORD{1000 + order_number}"


# # ---- Main Program ----
# price_per_item = 250
# quantity = int(input("Enter product quantity: "))

# if validate_quantity(quantity):
#     total_amount = calculate_total(price_per_item, quantity)
#     order_id = generate_order_id(1)

#     print("\nOrder Details")
#     print("Order ID:", order_id)
#     print("Quantity:", quantity)
#     print("Total Amount:", total_amount)
# else:
#     print("Invalid quantity! Quantity must be greater than 0.")

import random
import datetime

# ---------- Product Data ----------
PRODUCT_CATALOG = {
    "Laptop": 55000,
    "Headphones": 2500,
    "Keyboard": 1800,
    "Mouse": 900
}

# ---------- Validation ----------
def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than zero")

# ---------- Order ID Generator ----------
def generate_order_id():
    date_part = datetime.datetime.now().strftime("%Y%m%d")
    random_part = random.randint(1000, 9999)
    return f"ORD-{date_part}-{random_part}"

# ---------- Total Calculation ----------
def calculate_total(price, quantity):
    return price * quantity

# ---------- Main Order Process ----------
def place_order(product_name, quantity):
    if product_name not in PRODUCT_CATALOG:
        return "Product not available"

    try:
        validate_quantity(quantity)
    except ValueError as e:
        return str(e)

    price = PRODUCT_CATALOG[product_name]
    total_amount = calculate_total(price, quantity)
    order_id = generate_order_id()

    order_summary = {
        "Order ID": order_id,
        "Product": product_name,
        "Quantity": quantity,
        "Unit Price": price,
        "Total Amount": total_amount
    }

    return order_summary

# ---------- Execution ----------
product = input("Enter product name: ")
qty = int(input("Enter quantity: "))

result = place_order(product, qty)

print("\n--- Order Details ---")
if isinstance(result, dict):
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print(result)
