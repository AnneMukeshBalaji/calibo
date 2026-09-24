# Write a python program to count number of digits in a number.
def count_digits(n : int) -> int:
    if n == 0 : 
        return 1 
    if n < 0:
        n = n * -1
    sum = 0
    while(n > 0):
        sum += 1
        n = n // 10
    return sum
def main() -> None:
    n = int(input('Enter a Number : '))
    print(f'{n} has {count_digits(n)} digits')
if __name__ == "__main__":
    main()

