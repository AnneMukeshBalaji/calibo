from file1 import hello
def main() -> None:
    side_value = float(input("Enter the Side Value of a Square : "))
    area_of_square = compute_area_of_square(side_value)
    print(f'The Area Of the Square With Side Value : {side_value} is : {area_of_square}')
def compute_area_of_square(side_value) -> float:
    return side_value ** 2 # return keyword is used to return any kind of varaiables
if __name__ == "__main__":
    main()
    hello('Siva')
