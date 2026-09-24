# Write a python program to input salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary >  20000 : HRA = 30%, DA = 95%
def calculate_gross_salary(basic_salary: float) -> None:
    if basic_salary <= 10000:
        hra_percent = 20
        da_percent  = 80
    elif basic_salary <= 20000:
        hra_percent = 25
        da_percent  = 90
    else:
        hra_percent = 30
        da_percent  = 95
    hra          = (hra_percent / 100) * basic_salary
    da           = (da_percent  / 100) * basic_salary
    gross_salary = basic_salary + hra + da
    print(f"\n--- Salary Breakdown ---")
    print(f"Basic Salary  : Rs.{basic_salary:.2f}")
    print(f"HRA ({hra_percent}%)     : Rs.{hra:.2f}")
    print(f"DA  ({da_percent}%)     : Rs.{da:.2f}")
    print(f"Gross Salary  : Rs.{gross_salary:.2f}")
def main() -> None:
    basic_salary = float(input("Enter Basic Salary : "))
    if basic_salary <= 0:
        print("Basic Salary must be greater than zero.")
        return
    calculate_gross_salary(basic_salary)

if __name__ == "__main__":
    main()
