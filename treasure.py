import random


def create_treasure_file():
    digits = list(range(10))
    occurrences = [random.randint(1, 20) for _ in digits]

    try:
        with open('treasure.txt', 'w') as file:
            for digit, occurrence in zip(digits, occurrences):
                file.write(str(digit) * occurrence)
            file.write('TREASURE')

            for digit in reversed(digits):
                occurrence = random.randint(1, 20)
                file.write(str(digit) * occurrence)
    except IOError as e:
        print(f"Error occurred while creating treasure file: {str(e)}")


def play_treasure_hunt():
    try:
        with open('treasure.txt', 'r') as file:
            content = file.read()
    except IOError as e:
        print(f"Error occurred while reading treasure file: {str(e)}")
        return

    found = False
    position = 0

    while not found:
        user_input = input("Enter 'f' to move forward or 'b' to move backward: ")

        if user_input == 'f':
            position += 1
        elif user_input == 'b':
            position -= 1
        else:
            print("Invalid input. Please try again.")
            continue

        if position >= len(content):
            print("Congratulations! You found the treasure!")
            found = True
        else:
            print(content[position])


create_treasure_file()
play_treasure_hunt()





































