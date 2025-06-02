# Mini Games Collection

This repository includes **three fun and simple Python games**:
1. **Hangman**
2. **Rock, Paper, Scissors**
3. **Snake**

Each game is written using straightforward Python code (with Pygame used for the Snake game). Below is a brief overview of each:

---

## Hangman

A classic word-guessing game where the player tries to guess the letters of a hidden word before the hangman is fully drawn.

### How to Play:
- The game randomly selects a word from a predefined list (e.g., 'jail', 'cage', 'prison', 'containment').
- You guess letters one by one:
  - Correct guesses reveal part of the word.
  - Incorrect guesses increment the hangman drawing (up to 8 stages).
- If you guess all letters correctly, you win! Otherwise, you lose after 8 incorrect guesses.

---

## Rock, Paper, Scissors

A simple 3-round game against the computer.

### How to Play:
- The game prompts you to enter 'rock', 'paper', or 'scissor'.
- The computer randomly selects one of the three choices.
- The game determines the winner of each round and keeps score.
- After 3 rounds, it announces the winner or a tie.

---

## Snake

A simple Snake game using Pygame.

### How to Play:
- Use the arrow keys to control the snake’s direction (up, down, left, right).
- The snake grows each time it eats food.
- Avoid running into yourself or the screen edges.
- The game ends if the snake collides with itself or the wall.


### How to Run:
```bash
- python hangman.py
- python snake.py
- python rock.py

