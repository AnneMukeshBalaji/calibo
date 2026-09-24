# Write a python program to check whether a number is even or odd.
def is_odd(num : int) -> bool:
    if num % 2 != 0:
        return True
    else:
        return False
def main() -> None:
    num = int(input('Enter a number : '))
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")
if __name__ == "__main__":
    main()
