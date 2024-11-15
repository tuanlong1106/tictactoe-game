# Tic-Tac-Toe Game

This is an interactive Tic-Tac-Toe game developed using Python and Pygame. The game incorporates the minimax algorithm for decision-making to create a basic AI opponent.

## Features
- **Interactive Gameplay**: Play against the computer with an intuitive graphical user interface.
- **AI Opponent**: The AI uses the minimax algorithm to make optimal moves.
- **Modular Code**: The code is structured to be maintainable and easy to understand.

## Installation

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/tuanlong1106/tictactoe-game.git
cd tictactoe-game
```

### Step 2: Create a Virtual Environment
Create and activate a virtual environment to manage dependencies:
- **On macOS/Linux**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
- **On Windows**:
  ```bash
  python -m venv env
  .\env\Scripts\activate
  ```

### Step 3: Install Dependencies
Install the required dependencies using pip:
```bash
pip install pygame
```

## Usage
Run the game by executing the following command in the terminal:
```bash
python tictactoe.py
```

## How to Play
- The game starts with a main menu where you can select to start the game.
- The player uses 'X' and the AI uses 'O'.
- Click on an empty cell to make your move.
- The AI will automatically make its move after yours.
- The game will display the result and let you choose to play again or return to the main menu.

## Code Structure
- **`tictactoe.py`**: Contains the main game logic, including the Pygame setup, drawing functions, game loop, and the minimax algorithm.

## Future Improvements
- Add more difficulty levels for the AI.
- Implement a multiplayer mode.
- Enhance the user interface with more animations and effects.

---

Feel free to fork, modify, or contribute to this project. Enjoy playing Tic-Tac-Toe!
