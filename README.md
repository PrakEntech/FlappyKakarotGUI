# Flappy Kakarot

Flappy Kakarot is a simple game inspired by the popular Flappy Bird, where you control Goku (Kakarot) and navigate through obstacles. This game is developed using Python's Tkinter and PIL libraries for GUI and image handling.

## Features

- **Character Control**: Control Goku's movement using the 'W' key to dodge obstacles.
- **Score Tracking**: The game keeps track of your score and displays it in real-time. The highest score is saved between sessions.
- **Random Obstacles**: The game generates random obstacles for Goku to avoid, increasing the challenge as you progress.
- **Game Over Screen**: The game shows the final score when you collide with an obstacle.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (`pip install tk`)
- PIL (Pillow) (`pip install pillow`)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/PrakEntech/FlappyKakarotGUI.git
   cd FlappyKakarotGUI
   ```
2. **Run the game**:

   ```bash
   python main.pyw
   ```

## How to Play

- **Start the Game**: Click the "Start" button on the main menu.
- **Control Goku**: Press the 'W' key to make Goku fly upwards. The goal is to avoid the obstacles that appear on the screen.
- **Quit the Game**: You can exit the game by clicking the "Quit" button or by closing the window.
- **View High Score**: The highest score is displayed on the main menu and updates when a new high score is achieved.

## Game Structure

### `Do()`

The main game function that initializes the game components and handles the game loop.

### `Doit()`

This function is responsible for updating the game's state, including Goku's movement, collision detection, score updating, and generating new obstacles.

### `quitThis()`

Handles the end of the game when Goku collides with an obstacle. It checks if the current score is a new high score and saves it if necessary.

### UI Elements

- **Main Menu**: Consists of Start and Quit buttons, along with the highest score display.
- **Game Screen**: Displays the game background, obstacles, Goku, and the current score.
  
## Contact

For any inquiries, please contact me via:

- Instagram: [prak_entech983](https://www.instagram.com/prak_entech983/)
- YouTube: [Prak EnTech](https://www.youtube.com/c/PrakEnTech)
