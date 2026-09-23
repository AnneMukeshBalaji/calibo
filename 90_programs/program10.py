# Write a python program to check whether a character is uppercase or lowercase alphabet.
def check_character(character : str) -> None :
    if character.isalpha():
        if character.islower():
            print(f"{character} is a lower case alphabet")
        else :
            print(f"{character} is an upper case alphabet")
    else:
        print(f"{character} is not an alphabet")
def main() -> None:
    char = input('Enter an alphabet(single) : ')
    if len(char) > 1 :
        print('Enter only a single character')
        return
    check_character(char)
if __name__ == "__main__":
    main()
        
