# Write a python program to check whether a character is alphabet or not.
def is_alphabet(char:str) -> bool:
    if (char >= 'a' and char <='z') or (char >= 'A' and char <='Z'):
        return True
    else:
        return False
def main() -> None:
    char = input('Enter a single character : ')
    if len(char) > 1 :
        print('Enter only a single character')
        return
    if is_alphabet(char):
        print(f"{char} is an alphabet")
    else:
        print(f"{char} is not an alphabet")
if __name__ == "__main__":
    main()

