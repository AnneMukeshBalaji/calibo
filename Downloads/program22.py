# Write a python program to find sum of all natural numbers between 1 to n.
def sum_natural_numbers(n : int) -> int :
    sum = 0
    i = 1
    while (i <= n):
        sum += i
        i += 1
    return sum
def main() -> None:
    n = int(input('Enter a Natural Number : '))
    if n <= 0:
        print('Enter a valid Natural Number')
        return
    print(f"The sum of first {n} numbers is {sum_natural_numbers(n)}")
if __name__ == "__main__":
    main()
