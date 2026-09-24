#Write a python program to print all natural numbers from 1 to n. - using while loop
def print_natural_numbers(n :int) -> None :
    i = 1
    while i <= n :
        print(i)
        i += 1
def main() -> None:
    n = int(input("Enter a number : "))
    print_natural_numbers(n)
if __name__ == "__main__":
    main()