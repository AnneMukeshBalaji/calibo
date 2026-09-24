# Write a python program to find sum of all even numbers between 1 to n.
def sum_of_even_numbers(n:int)-> int :
    sum = 0
    i = 1
    while(i <= n):
        if i % 2 == 0:
            sum += i
        i += 1
    return sum
def main()-> None:
    n = int(input('Enter a natural number : '))
    if n <= 0 :
        print('Enter a valid natural number')
    print(f'sum of first {n} even natural numbers : {sum_of_even_numbers(n)}')
if __name__ == "__main__":
    main()
