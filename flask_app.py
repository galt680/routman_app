from flask import Flask

app = f.Flask(__name__)
@app.route("/")
def hello():
    return "Testing"


if __name__ == "__main__":
    app.run()
