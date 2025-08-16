from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

quiz = [
    {"question": "What animal meows?", "options": ["Cat", "Dog", "Lion", "Fish"], "answer": "Cat"},
    {"question": "What is the most popular phone brand in Asia?", "options": ["Motorolla", "iPhone", "Samsung", "Nokia"], "answer": "Samsung"},
    {"question": "Which 2019 anime has a central focus of fighting demons?", "options": ["Attack on Titan", "Frieren", "Demon Slayer", "Jujutsu Kaisen"], "answer": "Demon Slayer"}
]

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        score = 0

        for i, q in enumerate(quiz):
            if request.form.get(f"q{i}") == q["answer"]:
                score += 1
    return render_template("index.html", quiz=quiz)

@app.route('/result/<int:score>')
def result(score):
    return f"Your score is {score} out of {len(quiz)}"


if __name__ == "__main__":
    app.run(debug=True)