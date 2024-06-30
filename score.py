import os

# Constants
POINTS_OF_WINNING = lambda user_difficulty_select: (int(user_difficulty_select) * 3) + 5
SCORES_FILE_NAME = "scores.txt"

def add_score(user_difficulty_select):
    points = POINTS_OF_WINNING(user_difficulty_select)
    try:
        # Try to read the current score from the file
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
    except FileNotFoundError:
        # If the file does not exist, start with a score of 0
        current_score = 0
    except ValueError:
        # If the file content is invalid, start with a score of 0
        current_score = 0

    # Add the new points to the current score
    new_score = current_score + points

    # Save the new score back to the file
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))

    print(f"Score updated! Current score: {new_score}")

# Example usage:
# add_score(3)
