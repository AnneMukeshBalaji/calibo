# Write a python program to check whether a number is even or odd.
def is_odd(num : int) -> bool:
    if num % 2 == 1:
        return True
    else:
        return False
def main() -> None:
    num = int(input('Enter a number : '))
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is odd")
if __name__ == "__main__":
    main()
