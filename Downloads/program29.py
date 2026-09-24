# Write a python program to check whether a number is palindrome or not.
def check_palindrome(n) -> bool :
    if n < 0 : 
        n = -n
    n = str(n)
    first_pointer = 0
    last_pointer = len(n) - 1
    while (first_pointer <= last_pointer):
        if(n[first_pointer] != n[last_pointer]) :
            return False
        first_pointer += 1
        last_pointer -= 1
    return True    
def main() -> None:
    n = int(input("Enter a Number : "))
    if check_palindrome(n):
        print(f"{n} is a Palindrome")
    else:
        print(f"{n} is NOT a Palindrome")
if __name__ == "__main__":
        main()

