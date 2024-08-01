# World of Games: The Epic Journey

## Description
World of Games: The Epic Journey is a collection of simple, interactive games built in Python. This project was developed as part of a DevOps school curriculum and showcases various programming concepts and best practices.

## Games Included
1. **Memory Game**: A sequence of numbers will appear for 1 second, and you have to guess it back.
2. **Guess Game**: Guess a number and see if you chose like the computer.
3. **Currency Roulette**: Try and guess the value of a random amount of USD in ILS.

## Features
- Multiple games with varying difficulty levels
- Score tracking system
- Flask-based web server for displaying scores

## Installation

1. Clone the repository:

`git clone [URL]
`cd world-of-games`

2. Create a virtual environment (optional but recommended):
`python -m venv venv source venv/bin/activate #` 
`On Windows, use venv\Scripts\activate`

3. Install the required packages:
`pip install -r requirements.txt`

## Usage

1. Run the main game:
`python main.py`

2. Follow the on-screen prompts to select a game and difficulty level.

3. Play the selected game and try to win!

4. To view your score, run the Flask server:
`python main_score.py`
Then open a web browser and go to `http://localhost:5000`

## Project Structure

- `main.py`: The main entry point of the application
- `games.py`: Contains the central `play` function for all games
- `memory_game.py`: Logic for the Memory Game
- `guess_game.py`: Logic for the Guess Game
- `currency_roulette_game.py`: Logic for the Currency Roulette Game
- `score.py`: Handles score calculation and storage
- `main_score.py`: Flask server for displaying scores
- `utils.py`: Utility functions used across the project

## Contributing

Contributions to improve the games or add new features are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the DevOps Experts school for providing the project requirements and guidance.
- Shout out to all contributors who have helped improve this project.