# Write a python program to print all natural numbers in reverse (from n to 1). - using while loop
def reverse_loop(n : int) -> None :
    while(n >= 1):
        print(n)
        n -= 1
def main() -> None:
    n = int(input("Enter a positive integer : "))
    if n <= 0:
        print('Please enter a valid positive integer')
    reverse_loop(n)
if __name__ == "__main__":
    main()
            
