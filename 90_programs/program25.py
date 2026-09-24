# Write a python program to print multiplication table of any number.
def print_multiplication_table(n: int) -> None :
    i = 1
    while(i <= 10):
        print(f'{n} * {i} = {n * i}')
        i += 1
def main() -> None:
    n = int(input('Enter a Number : '))
    print_multiplication_table(n)
if __name__ == "__main__":
    main()
