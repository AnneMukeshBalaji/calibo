def is_divsible_by_5_and_11(num : int) -> bool:
    if num % 5 == 0 and num % 11 == 0 :
        return True
    else :
        return False
def main() -> None:
    num = int(input('Enter a number : '))
    if is_divsible_by_5_and_11(num) :
        print(f"{num} is divisible by both 5 and 11 ")
    else : 
        print(f"{num} is not divisible by both 5 and 11 ")

if __name__ == "__main__":
    main()
