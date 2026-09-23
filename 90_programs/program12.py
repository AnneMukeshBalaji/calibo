# Write a python program to count total number of notes in given amount.
def print_notes(amount: int) -> None:
    print("Number of Notes Required : ")
    if amount >= 500:
        notes_500 = amount // 500
        amount = amount % 500
        print(f"500 NOTES : {notes_500}")
 
    if amount >= 200:
        notes_200 = amount // 200
        amount = amount % 200
        print(f"200 NOTES : {notes_200}")
 
    if amount >= 100:
        notes_100 = amount // 100
        amount = amount % 100
        print(f"100 NOTES : {notes_100}")
 
    if amount >= 50:
        notes_50 = amount // 50
        amount = amount % 50
        print(f"50 NOTES : {notes_50}")
 
    if amount >= 20:
        notes_20 = amount // 20
        amount = amount % 20
        print(f"20 NOTES : {notes_20}")

    if amount >= 10:
        notes_10 = amount // 10
        amount = amount % 10
        print(f"10 NOTES : {notes_10}")

    if amount >= 5:
        coins_5 = amount // 5
        amount = amount % 5
        print(f"5 Coins : {coins_5}")

    if amount >= 2:
        coins_2 = amount // 2
        amount = amount % 2
        print(f"2 Coins : {coins_2}")

    if amount >= 1:
        coins_1 = amount // 1
        print(f"1 Coins : {coins_1}")


def main() -> None:
    amount = int(input("Enter a valid amount (> 0) : "))
    if amount <= 0:
        print("Enter a valid amount above zero")
        return
    print_notes(amount)


if __name__ == "__main__":
    main()
