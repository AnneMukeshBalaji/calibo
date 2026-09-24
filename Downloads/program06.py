# Write a python program to check whether a year is leap year or not.
def is_leap_year(year : int) -> bool : 
    if year  > 0 :
        if (year % 4 == 0 and  year % 100 != 0) or (year % 400 == 0) :
            return True
        else:
            return False
    else :
        return False
def main() -> None:
    year = int(input("Enter a year : "))
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
if __name__ == "__main__":
    main()
