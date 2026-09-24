# Write a python program to find first and last digit of a number.
def function_first_and_last(n:int) -> None :
    temp = n
    if temp < 0 :
        temp = temp * -1
    last_digit = temp % 10 
    while temp >= 10:
        temp = temp // 10
    print(f'first digit of {n} : {temp}\nlast digit of {n} : {last_digit}')
def main() -> None:
    n = int(input('Enter a Number : '))
    function_first_and_last(n)
if __name__ == "__main__":
    main()
