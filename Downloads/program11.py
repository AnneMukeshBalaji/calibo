# Write a python program to input week number and print week day.
def print_week_day(week_number :int) -> None :
    if week_number == 1 :
        print("Monday")
    elif week_number == 2 :
        print("Tuesday")
    elif week_number == 3 :
        print("Wednesday")
    elif week_number == 4 :
        print("Thursday")
    elif week_number == 5 :
        print("Friday")
    elif week_number == 6 :
        print("Saturday")
    elif week_number == 7 :
        print("Sunday")
    else :
        print("Not a Valid week Number")
def main() -> None:
    week_number = int(input("Enter a week Number : "))
    print_week_day(week_number)
if __name__ == "__main__":
    main()
