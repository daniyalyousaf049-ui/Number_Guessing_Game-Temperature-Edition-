import random
import time
import os

# ================================================
# Number Guessing Game - Temperature Edition
# ================================================

SCORE_FILE = "high_scores.txt"


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


def choose_difficulty():
    # simple difficulty menu -> changes range and number of tries
    print("\nChoose difficulty:")
    print("1. Easy   (1-50,  8 tries)")
    print("2. Medium (1-100, 7 tries)")
    print("3. Hard   (1-200, 6 tries)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 50, 8
    elif choice == "3":
        return 200, 6
    else:
        return 100, 7  # default = medium


def give_hint(secret, hints_used):
    # limited hint system: costs points but helps the player
    if hints_used >= 2:
        print("No more hints left for this round!")
        return hints_used

    if secret % 2 == 0:
        print("HINT: The number is EVEN.")
    else:
        print("HINT: The number is ODD.")

    hints_used += 1
    print(f"(Hints used: {hints_used}/2, each hint costs 5 points)")
    return hints_used


def play_round(player_name, max_range, max_tries):
    secret = random.randint(1, max_range)
    tries = 0
    hints_used = 0
    start_time = time.time()

    print(f"\n--- {player_name}'s turn ---")
    print(f"Guess the number between 1 and {max_range}. You have {max_tries} tries.")
    print("Type 'hint' instead of a number if you want a clue (max 2 hints).")

    while tries < max_tries:
        guess_input = input("Enter your guess: ").strip().lower()

        if guess_input == "hint":
            hints_used = give_hint(secret, hints_used)
            continue

        if not guess_input.isdigit():
            print("Please enter a valid number (or 'hint').")
            continue

        guess = int(guess_input)
        tries += 1

        if guess == secret:
            time_taken = round(time.time() - start_time, 1)
            print(f"Correct! {player_name} got it in {tries} tries and {time_taken} seconds.")

            base_score = max(0, (max_tries - tries) * 10 + 20)
            hint_penalty = hints_used * 5
            score = max(0, base_score - hint_penalty)

            print(f"Score: {base_score} - {hint_penalty} (hint penalty) = {score}")
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


def load_high_scores():
    # reads saved scores from file, returns a dictionary {name: best_score}
    scores = {}
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if "," in line:
                    name, value = line.split(",")
                    scores[name] = int(value)
    return scores


def save_high_scores(scores):
    # overwrites the file with the current best scores
    with open(SCORE_FILE, "w") as f:
        for name, value in scores.items():
            f.write(f"{name},{value}\n")


def update_high_scores(current_scores):
    # merges this session's scores with saved best scores
    saved = load_high_scores()

    for name, score in current_scores.items():
        if name not in saved or score > saved[name]:
            saved[name] = score

    save_high_scores(saved)
    return saved


def show_scoreboard(title, scores_dict):
    print(f"\n=== {title} ===")
    sorted_scores = sorted(scores_dict.items(), key=lambda x: x[1], reverse=True)

    medals = ["1st", "2nd", "3rd"]
    for i, (name, score) in enumerate(sorted_scores):
        tag = medals[i] if i < 3 else f"{i+1}th"
        print(f"{tag} - {name}: {score} points")


def main():
    print("=== NUMBER GUESSING GAME (Temperature Edition) ===")

    while True:
        num_players = input("How many players? (1-4): ")
        if num_players.isdigit() and 1 <= int(num_players) <= 4:
            num_players = int(num_players)
            break
        print("Enter a number between 1 and 4.")

    max_range, max_tries = choose_difficulty()

    scores = {}
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ").strip()
        if name == "":
            name = f"Player {i+1}"
        scores[name] = play_round(name, max_range, max_tries)

    show_scoreboard("FINAL SCOREBOARD (This Session)", scores)

    winner = max(scores, key=scores.get)
    print(f"\n{winner} wins the round! Congratulations.")

    all_time = update_high_scores(scores)
    show_scoreboard("ALL-TIME HIGH SCORES", all_time)


if __name__ == "__main__":
    main()

    winner = sorted_scores[0][0]
    print(f"\n{winner} wins the round! Congratulations.")


if __name__ == "__main__":
    main()
