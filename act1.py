import random

def roll_dice(num_dice):
    """Rolls a specified number of six-sided dice.

    Args:
        num_dice: The number of dice to roll.

    Returns:
        A list of the rolled values.
    """

    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        rolls.append(roll)
    return rolls

def main():
    """The main game loop."""

    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? (0 to quit): "))

            if num_dice == 0:
                print("Thanks for playing!")
                break

            if num_dice < 0:
                raise ValueError("Please enter a non-negative number of dice.")

            rolls = roll_dice(num_dice)
            print("You rolled:", rolls)

        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()