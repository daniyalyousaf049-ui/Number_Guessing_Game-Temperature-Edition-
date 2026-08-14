# Number Guessing Game - Temperature Edition

A Python-based interactive number guessing game with a unique temperature-based hint system, multiplayer support, and persistent high score tracking. Developed as a Programming Fundamentals Lab Project.

## 🎮 Game Overview

The Number Guessing Game challenges players to guess a randomly generated number within a specified range. Unlike traditional "higher/lower" games, this edition provides **temperature-based hints** (e.g., "Burning Hot," "Freezing Cold") to make the experience more engaging and intuitive.

Players can compete against friends in local multiplayer sessions, use strategic hints to narrow down possibilities, and track their best scores across multiple game sessions.

---

## ✨ Features

### 🔥 Temperature-Based Hint System
- Get descriptive hints based on how close your guess is to the secret number:
  - **Burning Hot** (≤2% away)
  - **Very Hot** (≤5% away)
  - **Warm** (≤12% away)
  - **Cold** (≤25% away)
  - **Freezing Cold** (>25% away)

### 🧠 Strategic Hint System
- Players can request up to **2 hints per round**
- Hints reveal whether the number is **even** or **odd**
- Each hint costs **5 points** from the final score (penalty system)

### 👥 Multiplayer Support
- Supports **1-4 players** in local multiplayer mode
- Each player takes turns guessing the same number
- Session scoreboard displays rankings

### 📊 Persistent High Scores
- Scores are saved to `high_scores.txt`
- All-time leaderboard tracks the best score per player
- Automatically merges new session scores with existing records

### 🎯 Difficulty Levels
| Difficulty | Number Range | Tries |
|------------|--------------|-------|
| Easy       | 1-50         | 8     |
| Medium     | 1-100        | 7     |
| Hard       | 1-200        | 6     |

### ⏱️ Performance Metrics
- Tracks **time taken** to guess correctly
- Displays **number of tries** used
- Calculates **score** based on remaining tries and hint penalties

---

## 📋 Scoring System

```
Base Score = (Max Tries - Tries Used) × 10 + 20
Final Score = max(0, Base Score - (Hints Used × 5))
```

- Players earn higher scores by guessing with fewer tries
- Using hints reduces the final score (5 points per hint)
- Score cannot go below 0

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external libraries required

### Installation
1. Clone the repository or download the script:
```bash
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game
```

2. Run the game:
```bash
python number_guessing_game.py
```

### How to Play
1. **Enter the number of players** (1-4)
2. **Choose a difficulty level** (Easy/Medium/Hard)
3. **Enter player names** (or press Enter for default names)
4. **Take turns guessing** the secret number
5. Type `hint` to reveal if the number is even or odd (max 2 hints)
6. After all players have guessed, view the session scoreboard and all-time rankings

---

## 📁 File Structure

```
number-guessing-game/
├── number_guessing_game.py    # Main game script
├── high_scores.txt            # Persistent high score storage (auto-generated)
└── README.md                  # Project documentation
```

---

## 🛠️ Code Architecture

### Core Functions

| Function | Description |
|----------|-------------|
| `get_temperature(diff, max_range)` | Returns temperature-based hint based on guess proximity |
| `choose_difficulty()` | Displays difficulty menu and returns range/tries |
| `give_hint(secret, hints_used)` | Provides even/odd hint with penalty tracking |
| `play_round(player_name, max_range, max_tries)` | Main game logic for a single player's turn |
| `load_high_scores()` | Reads saved scores from file |
| `save_high_scores(scores)` | Writes scores to file |
| `update_high_scores(current_scores)` | Merges session scores with all-time records |
| `show_scoreboard(title, scores_dict)` | Displays ranked scoreboard with medals |

---

## 🎯 Game Flow

```
Start
  ↓
Set number of players (1-4)
  ↓
Select difficulty level
  ↓
For each player:
  ↓
  Guess the secret number
  ├── Receive temperature hints
  ├── Optionally use even/odd hint
  └── Score calculated based on performance
  ↓
Display session scoreboard
  ↓
Declare winner
  ↓
Update and display all-time high scores
```

---

## 🧪 Testing

The game includes robust input validation:
- Validates player count (1-4)
- Ensures numeric guesses
- Handles 'hint' command properly
- Prevents invalid difficulty choices
- Sanitizes empty player names

---

## 🔧 Customization

### Modifying Difficulty Levels
Edit the `choose_difficulty()` function to adjust ranges and tries:
```python
if choice == "1":
    return 50, 8    # Change range or tries as needed
```

### Adjusting Hint Penalty
Modify the hint penalty value in `play_round()`:
```python
hint_penalty = hints_used * 5  # Change '5' to desired penalty
```

### Temperature Thresholds
Adjust proximity percentages in `get_temperature()`:
```python
if percent <= 2:      # "Burning Hot" threshold
    return "BURNING HOT!! you are almost there"
```

---

## 📝 Future Improvements

- [ ] Add GUI interface (Tkinter/PyGame)
- [ ] Implement online multiplayer
- [ ] Add more hint types (prime numbers, divisible by X)
- [ ] Include difficulty-based scoring multipliers
- [ ] Add sound effects for guessing feedback
- [ ] Support for custom number ranges

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is created for educational purposes as part of a Programming Fundamentals Lab Project.


---

## 🙏 Acknowledgments

- Inspired by classic number guessing games
- Temperature hint mechanic adds educational value about percentages
- Designed to practice Python fundamentals: functions, file I/O, loops, conditionals, and data structures

---

## 📞 Support

For questions, suggestions, or bug reports, please open an issue on the GitHub repository or contact the development team.

---

**Enjoy the game! 🎉 Happy guessing!**
