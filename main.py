import random


def convert_distance():
    distance = float(input("Enter the distance: "))
    unit = input("Enter the unit (millimeter, centimeter, meter, kilometer): ")
    while unit not in ["millimeter", "centimeter", "meter", "kilometer"]:
        unit = input("Enter the unit (millimeter, centimeter, meter, kilometer): ").strip().lower()
    if unit == "millimeter":
        converted_distance = distance / 10
        converted_unit = "centimeter"
    elif unit == "centimeter":
        converted_distance = distance / 100
        converted_unit = "meter"
    elif unit == "meter":
        converted_distance = distance / 1000
        converted_unit = "kilometer"
    elif unit == "kilometer":
        converted_distance = distance * 100000
        converted_unit = "centimeter"

    print(f"{distance} {unit}(s) is equal to {converted_distance} {converted_unit}(s).")


def find_largest_and_smallest():
    numbers = []
    N = int(input("Enter the number of elements: "))
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    largest = numbers[0]
    largest_index = 0
    smallest = numbers[0]
    smallest_index = 0

    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
            largest_index = i
        if numbers[i] <= smallest:
            smallest = numbers[i]
            smallest_index = i

    print(f"The largest number is {largest} at index {largest_index}")
    print(f"The smallest number is {smallest} at index {smallest_index}")


def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter what you want (R for Rock, P for Paper, S for Scissors): ")

        if user_choice not in ['R', 'P', 'S']:
            print("Choose R for Rock, P for Paper, S for Scissors, no other options")
            continue

        computer_choice = random.choice(['R', 'P', 'S'])
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("draw.")
        elif ((user_choice == 'R' and computer_choice == 'S') or (user_choice == 'P' and computer_choice == 'R') or
              (user_choice == 'S' and computer_choice == 'P')):
            user_score += 1
            print("User won this round!")
        else:
            computer_score += 1
            print("Computer won this round!")

        print(f"Score is --> User: {user_score}, Computer: {computer_score}")

        if user_score == 5:
            print("User won the game")
            break
        elif computer_score == 5:
            print("Computer won the game")
            break


if __name__ == "__main__":
    """ uncomment the function which you want to check and run the program """
    # convert_distance()
    # find_largest_and_smallest()
    # rock_paper_scissors_game()
    pass