from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!<h1>'


def make_bold(function):
    def wrapper_func():
        return f"<u>{function()}</u>"
    return wrapper_func

def make_emphasis(function):
    def wrapper_func():
        return f"<u>{function()}</u>"
    return wrapper_func

def make_underline(function):
    def wrapper_func():
        return f"<u>{function()}</u>"
    return wrapper_func

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'bye'


# Creating variables paths
@app.route('/username/<name>')
def greet(name):
    return  f"<h1>Hello, {name}!<h1>"

if __name__ == "__main__":
    app.run(debug=True)