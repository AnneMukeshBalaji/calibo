# Write a python program to find maximum between three numbers
def find_max(num1:int,num2:int,num3:int) -> int :
    if num1 > num2 and num1 > num3 :
        return num1 
    elif num2 > num1 and num2 > num3 :
        return num2 
    else :
        return num3
def main() -> None:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    num3 = int(input("Enter Number 3 : "))
    print(f"Max among three numbers is {find_max(num1,num2,num3)}")
if __name__ == "__main__":
    main()
