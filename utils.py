import os
SCORES_FILE_NAME = "scores.txt"
with open(SCORES_FILE_NAME, 'r') as file:
    content = file.read()
    print(content)

BAD_RETURN_CODE = 4004

def screen_cleaner():
    # Check if the system is Windows or Unix-based
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Unix/Linux/MacOS
        os.system('clear')