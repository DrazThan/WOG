from flask import Flask, render_template

app = Flask(__name__)

SCORES_FILE_NAME = "scores.txt"

def read_score():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
            return int(score)
    except (FileNotFoundError, ValueError) as e:
        return None

@app.route('/')
def score_server():
    score = read_score()
    if score is None:
        error_message = "Error: Could not read the score."
        return render_template('index.html', error_message=error_message)
    else:
        return render_template('index.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
