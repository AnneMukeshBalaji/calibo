# Write a python program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units      : Rs. 0.50/unit
# For next 100 units      : Rs. 0.75/unit  (51  - 150)
# For next 100 units      : Rs. 1.20/unit  (151 - 250)
# For units above 250     : Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
def calculate_electricity_bill(units: int) -> None:
    if units <= 50:
        bill = units * 0.50

    elif units <= 150:
        bill = (50 * 0.50) + ((units - 50) * 0.75)

    elif units <= 250:
        bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)

    else:
        bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

    surcharge = 0.20 * bill
    total     = bill + surcharge

    print(f"\n--- Electricity Bill ---")
    print(f"Units Consumed : {units}")
    print(f"Bill Amount    : Rs. {bill:.2f}")
    print(f"Surcharge (20%): Rs. {surcharge:.2f}")
    print(f"Total Bill     : Rs. {total:.2f}")

def main() -> None:
    units = int(input("Enter units consumed : "))
    if units < 0:
        print("Units cannot be negative.")
        return
    calculate_electricity_bill(units)

if __name__ == "__main__":
    main()
