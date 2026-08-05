import random

# Number Guessing Game - Temperature Edition
# PF Lab Project

def get_temperature(diff, max_range):
    # gives a hot/cold style hint instead of boring "too high/too low"
    percent = (diff / max_range) * 100

    if percent <= 2:
        return "BURNING HOT!! you are almost there"
    elif percent <= 5:
        return "Very Hot"
    elif percent <= 12:
        return "Warm"
    elif percent <= 25:
        return "Cold"
    else:
        return "Freezing Cold, try again"


def play_round(player_name, max_range=100, max_tries=7):
    secret = random.randint(1, max_range)
    tries = 0
    print("\n---", player_name + "'s turn ---")
    print(f"Guess the number between 1 and {max_range}. You have {max_tries} tries.")

    while tries < max_tries:
        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_input)
        tries += 1

        if guess == secret:
            print(f"Correct! {player_name} got it in {tries} tries.")
            score = max(0, (max_tries - tries) * 10 + 20)
            return score

        diff = abs(secret - guess)
        hint = get_temperature(diff, max_range)

        # extra twist: also tells if guess is high or low, but only after 3 wrong tries
        if tries >= 3:
            direction = "too high" if guess > secret else "too low"
            print(f"{hint} ({direction})")
        else:
            print(hint)

        print(f"Tries left: {max_tries - tries}")

    print(f"Out of tries! The number was {secret}.")
    return 0


def main():
    print("=== NUMBER GUESSING GAME (Temperature Edition) ===")
    num_players = 4
    scores = {}

    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        if name.strip() == "":
            name = f"Player {i+1}"
        scores[name] = play_round(name)

    print("\n=== FINAL SCOREBOARD ===")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    rank = 1
    for name, score in sorted_scores:
        print(f"{rank}. {name} - {score} points")
        rank += 1

    winner = sorted_scores[0][0]
    print(f"\n{winner} wins the round! Congratulations.")


if __name__ == "__main__":
    main()
