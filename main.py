from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        output = function()
        output = f"<b>{output}<b>"
        return output

    return wrapper_function


@app.route("/")
@make_bold
def home():
    return "welcome to home"


if __name__ == "__main__":
    app.run(debug=True)


