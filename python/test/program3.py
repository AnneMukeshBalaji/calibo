# Inventory Management System Using Dictionary
# A small retail store wants to manage its inventory. Each product has a product ID, product name, price, and available quantity.
# Write a Python program using a dictionary to perform inventory analysis and generate a customer bill.
# Given Data:
# inventory = {
#     101: {"name": "Laptop", "price": 55000, "quantity": 5},
#     102: {"name": "Mouse", "price": 800, "quantity": 20},
#     103: {"name": "Keyboard", "price": 1500, "quantity": 10},
#     104: {"name": "Monitor", "price": 12000, "quantity": 3},
#     105: {"name": "Headphones", "price": 2000, "quantity": 8}
# }
# Requirements
# Display all products with their ID, name, price, and quantity.
# Calculate and display the total inventory value.
# Formula:
# price × quantity
# Find and display the most valuable product in the inventory.
# Formula:
# price × quantity
# Display products whose quantity is less than 5.
# Display products whose price is greater than ₹2,000.
# Accept a product ID and purchase quantity from the user.
# Check whether the product exists in the inventory.
# Check whether the requested quantity is available.
# If available:
# Calculate the purchase amount.
# Update the product's quantity.
# Display the purchase details.
# If the product does not exist or the quantity is insufficient, display an appropriate message.
# Display the updated inventory after the purchase.

def display(a) -> None :
    print(a)

def total_value(a) -> None:
    total = 0
    for i in a :
        total += a[i]["price"] * a[i]["quantity"]
    print("Total Value of the Inventory : ",total)

def most_valuable_item(a) -> None:
    max = 0
    max_name = ""
    for i in a :
        val = a[i]["price"] * a[i]["quantity"]
        if val > max :
            max = val
            max_name = a[i]["name"]
    print(f'Valuable Product is : {max_name} with value : {max} ')

def display_product_With_quantity(a,val):
    print("Products with quantity less than",val," : ")
    for i in a :
        if a[i]["quantity"] < val :
            print(a[i]["name"])

def price_greather_than_val(a,val):
    print("Products with price greater than ",val," : ")
    for i in a :
        if a[i]['price'] > val :
            print(a[i]["name"])

def accept_input(a):
    product_id = int(input("Enter Product ID : "))
    purchase_quantity = int(input("Enter purchase quantity : "))
    for i in a :
        if i == product_id :
            print("Total Value : ",a[i]["price"] * purchase_quantity)

def check_item(a,product_id):
    for i in a :
        if i == product_id :
            print("Product exist")
            return
    print("Product do not exist")

def requested_quantity(a,product_id,requested_quantity_of_item):
    for i in a :
        if  i == product_id and a[i]['quantity'] >= requested_quantity_of_item:
            print("Total Bill : ",(a[i]['quantity'] * a[i]['price']))
        elif i == product_id and a[i]['quantity'] < requested_quantity_of_item :
            print("Requested quantity not available , Available quantity : ",a[i]['quantity'])

def main() -> None:
    inventory = {
        101: {"name": "Laptop", "price": 55000, "quantity": 5},
        102: {"name": "Mouse", "price": 800, "quantity": 20},
        103: {"name": "Keyboard", "price": 1500, "quantity": 10},
        104: {"name": "Monitor", "price": 12000, "quantity": 3},
        105: {"name": "Headphones", "price": 2000, "quantity": 8}
    }
    display(inventory)
    total_value(inventory)
    most_valuable_item(inventory)
    display_product_With_quantity(inventory,5)
    price_greather_than_val(inventory,2000)
    accept_input(inventory)
    check_item(inventory,101)
    requested_quantity(inventory,102,21)

if __name__ == "__main__":
    main()
