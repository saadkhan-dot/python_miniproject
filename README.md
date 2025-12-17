# Liars Game – Python Mini Project

## 📌 Project Overview
This is a beginner-level Python mini project that implements a simple **Liar’s Game** using logical reasoning and user input.  
Players answer a yes/no question in each round, and the **minority group wins the round**. Scores are tracked across multiple rounds to determine the final winner(s).

---

## 🎯 Objectives
- Practice Python fundamentals
- Improve logical reasoning and decision-making
- Work with loops, conditions, lists, and user input
- Validate user input to avoid incorrect entries

---

## 🛠 Concepts Used
- Variables and data types  
- `if-else` conditional statements  
- `for` and `while` loops  
- Lists and list operations  
- Input validation  
- Score tracking logic  
- `enumerate()` for finding winners  

---

## ⚙️ How the Game Works
1. The user enters the number of players and rounds.
2. In each round:
   - A yes/no question is entered.
   - Each player answers either **yes** or **no**.
   - Input is validated to accept only yes or no.
3. The group with fewer players (minority) wins the round.
4. Points are awarded to players in the minority group.
5. After all rounds, final scores and winner(s) are displayed.

---

## ▶️ How to Run
1. Make sure Python 3 is installed.
2. Clone this repository or download the file.
3. Run the program using:
   ```bash
   python liars_game.py
