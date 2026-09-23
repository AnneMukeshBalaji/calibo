# Write a python program to check whether a number is negative, positive or zero.
def check_number(num : int) -> str:
    if num > 0 :
        return "Positive"
    elif num == 0:
        return "zero"
    else :
        return "negative"
def main() -> None:
    num = int(input('Enter a number : '))
    print(f"The Given Number is {check_number(num)}")

if __name__ == "__main__":
    main()
