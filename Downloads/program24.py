# Write a python program to find sum of all odd numbers between 1 to n.
def sum_of_odd_numbers(n:int)->int :
    sum = 0
    i = 0
    while(i <= n):
        if i % 2 == 1:
            sum += i
        i += 1
    return sum 
def main() -> None:
    n = int(input('Enter a valid natural number : '))
    if n <= 0 :
        print('Please Enter a valid natural number')
        return
    print(f'sum of first {n} odd natural numbers is : {sum_of_odd_numbers(n)}')
if __name__ =="__main__":
    main()
