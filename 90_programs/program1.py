# Write a python program to find maximum between two numbers.
def find_max(num1 : int ,num2 : int) -> int :
    return num1 if num1 > num2 else num2
def main() -> None:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    print(f"Max Number is : {find_max(num1,num2)}")
if __name__ == "__main__":
    main()
