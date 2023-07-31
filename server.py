from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def guess():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \

@app.route('/<int:number>')
def guess_number(number):
    if number == random_number:
        return '<h1 style="color:green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/xT5LMR5B0fQJe5S5nW/giphy.gif">'
    elif number < random_number:
        return '<h1 style="color:red">Too low try again!</h1>' \
               '<img src="https://media.giphy.com/media/hCkleYLj5mQJj9xRXZ/giphy.gif">'
    else:
        return '<h1 style="color:blue">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/l41JGlWa1xOjJSsV2/giphy.gif">'










if __name__ == "__main__":
    app.run(debug=True)