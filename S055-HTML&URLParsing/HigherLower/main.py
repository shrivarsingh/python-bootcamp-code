from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def welcome():
    return '<h1 style="color: blue">Guess a number between 0 and 9.</h1>' \
           '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif">' \
           f'<h1>{number}</h1>' \


@app.route('/<int:url_number>')
def check_number(url_number):
    if url_number == number:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/10UB1BfC4EKll6/giphy.gif">'
    elif url_number < number:
        return '<h1 style="color: red">Too low</h1>' \
               '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif">'
    else:
        return '<h1 style="color: purple">Too high</h1>' \
               '<img src="https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif">'


if __name__ == "__main__":
    number = (random.randint(0, 9))
    app.run(debug=True)