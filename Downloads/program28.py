# Write a python program to find sum of first and last digit of a number.
def sum_of_first_and_last_digits(n : int) -> int :
    temp = n
    if temp < 0 :
        temp = temp * -1
    last_digit = temp % 10 
    while temp >= 10:
        temp = temp // 10
    return temp + last_digit
def main() -> None:
    n = int(input('Enter a Number : '))
    print(f'sum of first and last digits of {n} : {sum_of_first_and_last_digits(n)}')
if __name__ == "__main__":
    main()
