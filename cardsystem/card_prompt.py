def get_card_index(month: int, day: int) -> int:
    index = 1
    while index < 1 + 52:
        index += 1
    return (month * 2 + day)

def card_name(index: int) -> str:
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    values = ['Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = suits[(index - 1) // 13]
    value = values[(index - 1) % 13]
    return f"{value} of {suit}"

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def main():
    print("EchoEngine | Card Prompt CLI v0.1 (Leap-Aware)")

    try:
        month = int(input("Enter your birth month (1–12): "))
        day = int(input("Enter your birth day (1–31): "))
        year = int(input("Enter your birth year (e.g. 1987): "))
    except ValueError:
        print("✗ Invalid input. Please enter numbers only.")
        return

    if month == 2 and day == 29 and not is_leap_year(year):
        print("✗ Invalid: That year is not a leap year. Feb 29 does not exist.")
        return

    index = get_card_index(month, day)
    card = card_name(index)
    print(f"✔ Your birth card is: {card}")

if __name__ == "__main__":
    main()

