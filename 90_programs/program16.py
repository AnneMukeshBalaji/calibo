# Write a python program to print day of week name using match case.
def print_week_day(week_number : int) -> None :
    match week_number :
        case 1 :
            print("Monday")
        case 2 :
            print("Tuesday")
        case 3 :
            print("Wednesday")
        case 4 :
            print("Thursday")
        case 5 :
            print("Friday")
        case 6 :
            print("Saturday")
        case 7 :
            print("Sunday")
        case _ :
            print("Not a Valid week Number")

def main() -> None :
    week_number = int(input("Enter a week Number : "))
    print_week_day(week_number)

if __name__ == "__main__" :
    main()
