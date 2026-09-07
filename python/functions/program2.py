# write a python program to create a function calculate_bill() that accepts customer number, customer name, and electricity units consumed as arguments.
# the function should calculate the electricity bill based on the following slab rates and return the final bill amount.
# requirements:
# take customer number, customer name, and units consumed from the user.
# create a function with three parameters.
# pass all three values as arguments while calling the function.
# calculate the bill inside the function using the following slab rates:
# units consumed	rate per unit
# first 100 units	₹2
# next 100 units (101–200)	₹3
# next 200 units (201–400)	₹5
# above 400 units	₹7
# calculate the bill using progressive slab calculation.
# return the final bill amount from the function.
# display the customer details and bill amount in the calling program.
# the function should not use print() to display the final bill.
# example input:
# enter customer number: 101
# enter customer name: rahul
# enter units consumed: 350
# expected output:
# --- electricity bill ---
# customer number: 101
# customer name: rahul
# units consumed: 350
# total bill: ₹1250

def main() -> None:
    customer_number = int(input("enter customer number : "))
    customer_name = input("enter customer name : ")
    units_consumed = int(input("enter number of units consumed : "))
    cbill = calculate_bill(units_consumed)
    print("\n--- Electricity Bill ---")
    print(f"Customer Number : {customer_number}")
    print(f"Customer Name   : {customer_name}")
    print(f"Units Consumed  : {units_consumed}")
    print(f"Total Bill      : ₹{cbill}")
def calculate_bill(units_consumed) -> float:
    cbill = 0
    if units_consumed <= 100 :
        cbill = units_consumed * 2
    elif units_consumed > 100 and units_consumed <= 200 :
        cbill = 100 * 2 + (units_consumed - 100) * 3
    elif units_consumed > 200 and units_consumed <= 400 :
        cbill = 100 * 2 + 100 * 3 + (units_consumed - 200) * 5 
    else : 
        cbill = 100 * 2 + 100 * 3 + 200 * 5 + (units_consumed - 400) * 7 
    return cbill

if __name__ == "__main__":
    main()
