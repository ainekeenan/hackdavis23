from flask import Flask

app = Flask(__name__)

@app.route("/CATS")

def hello_world():
    return "<p>Hello, World! CATSJKLSKLKLJSLSK</p>"


if  __name__ == '__main__':
    app.run()

