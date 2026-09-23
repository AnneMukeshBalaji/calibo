# Write a python to input any character and check whether it is alphabet, digit or special character.
def check_character(character : str) -> None :
    if character.isalpha():
        print(f"{character} is an alphabet")
    elif character.isdigit():
        print(f"{character} is a digit")
    else :
        print(f"'{character}' is a special character")

def main() -> None:
    char = input('Enter an character(single) : ')
    if len(char) > 1 :
        print('Enter only a single character')
        return
    check_character(char)
if __name__ == "__main__":
    main()
