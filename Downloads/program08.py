# Write a python program to input any alphabet and check whether it is vowel or consonant.
def is_vowel(char: str) -> str:
    vowels = ['a','e','i','o','u']
    if char.lower() in vowels :
        return "vowel" 
    else:
        if char.lower() >= 'a' and char.lower() <='z':
            return "consonant"
        else:
            return "not an alphabet"
def main() -> None:
    char = input('Enter an alphabet(single) : ')
    if len(char) > 1 :
        print('Enter only a single character')
        return
    print(f"{char} is {is_vowel(char)}")
if __name__ == "__main__":
    main()
