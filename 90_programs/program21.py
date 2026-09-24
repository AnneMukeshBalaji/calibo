# Write a python program to print all odd number between 1 to 100.
def print_odd_number() -> None:
    i = 1
    while(i <= 100):
        if i % 2 == 1:
            print(i)
        i += 1
if __name__ == "__main__":
    print_odd_number()
