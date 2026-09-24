# Write a python program to print all even numbers between 1 to 100. - using while loop 
def print_even_numbers() -> None:
    i = 1
    while(i <= 100):
        if i % 2 == 0:
            print(i)
        i += 1
if __name__ =="__main__":
    print_even_numbers()
