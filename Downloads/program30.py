# Write a python program to calculate sum of digits of a number.
def sum_of_digits(n:int) -> int :
    if n < 0 :
         n = -n
    sum = 0
    while(n > 0):
        digit = n % 10 
        sum += digit 
        n = n // 10
    return sum
def main() -> None:
    n = int(input("Enter a Number : "))
    print(f'sum of digits of {n} is : {sum_of_digits(n)}')
if __name__ == "__main__":
        main()

